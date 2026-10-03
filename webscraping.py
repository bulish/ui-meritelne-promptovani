import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
import random
import time
import os
import re

# Nastavení URL a parametrů
BASE_URL = "https://is.mendelu.cz/zp/portal_zp.pl"
OUTPUT_DIR = "stazene_prace"

# Seznam let, která chceme procházet
YEARS_TO_SCRAPE = ['2026', '2025', '2024', '2023', '2022'] 

# Vytvoření složky pro stažené soubory
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Použijeme Session
session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
})

def get_filename_from_headers(response, default_name):
    """Pokusí se vytáhnout originální název souboru z hlaviček serveru."""
    cd = response.headers.get('content-disposition')
    if cd:
        match = re.search(r'filename="?([^"]+)"?', cd)
        if match:
            return match.group(1)
    return default_name

def scrape_theses():
    for year in YEARS_TO_SCRAPE:
        print(f"\n--- Zpracovávám rok: {year} ---")
        
        form_data = {
            'pracoviste': '1', 
            'typ': ['102', '1', '2', '3', '101', '5'], 
            'obdobi': year,
            'jazyk': '3', # 3 = English
            'zobrazit': 'Display',
            'prehled': 'pracoviste'
        }

        try:
            # 1. KROK: Odeslání formuláře
            response = session.post(BASE_URL, data=form_data)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            # Hledání ID prací
            detail_links = soup.find_all('a', title="Displaying the final thesis")
            
            zp_ids = []
            for link in detail_links:
                href = link.get('href', '')
                match = re.search(r'zp=(\d+)', href)
                if match:
                    zp_ids.append(match.group(1))

            zp_ids = list(set(zp_ids))
            print(f"Nalezeno {len(zp_ids)} anglických prací pro rok {year}.")

            if not zp_ids:
                continue

            # 2. KROK: Výběr 10 náhodných prací
            selected_ids = random.sample(zp_ids, min(10, len(zp_ids)))
            
            # 3. KROK: Stažení
            for idx, zp_id in enumerate(selected_ids, 1):
                print(f"  [{idx}/10] Stahuji práci s ID {zp_id}...")
                
                download_url = f"https://is.mendelu.cz/zp/portal_zp.pl?prehled=pracoviste;zp={zp_id};download_prace=1"
                
                try:
                    file_res = session.get(download_url, stream=True)
                    file_res.raise_for_status() 
                    
                    # Získání původního názvu ze serveru
                    original_name = get_filename_from_headers(file_res, "thesis.pdf")
                    # Očištění názvu od speciálních znaků
                    original_name = "".join(c for c in original_name if c.isalnum() or c in (' ', '.', '_', '-')).rstrip()
                    
                    # OPRAVA: Vynucené vložení ROKU a ID na začátek názvu souboru
                    final_filename = f"{year}_{zp_id}_{original_name}"
                    filepath = os.path.join(OUTPUT_DIR, final_filename)
                    
                    # Zápis souboru na disk
                    with open(filepath, 'wb') as f:
                        for chunk in file_res.iter_content(chunk_size=8192):
                            f.write(chunk)
                    print(f"      -> Uloženo jako: {final_filename}")
                    
                except HTTPError as e:
                    print(f"      -> CHYBA: Práci {zp_id} nelze stáhnout (Chyba {e.response.status_code}). Pravděpodobně je skrytá. Přeskakuji...")
                except Exception as e:
                    print(f"      -> NEČEKANÁ CHYBA u práce {zp_id}: {e}")

                time.sleep(1.5)
                
        except Exception as e:
             print(f"Chyba při zpracování roku {year}: {e}")

if __name__ == "__main__":
    scrape_theses()
    print("\nHotovo! Všechny dostupné práce jsou staženy ve složce:", OUTPUT_DIR)