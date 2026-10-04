import os
import re
from pathlib import Path
from pypdf import PdfReader, PdfWriter

OLD_INPUT_DIR = "stazene_prace"
INPUT_DIR = "stazene_prace_s_abstraktem"
OUTPUT_DIR = "stazene_prace_bez_abstraktu"

# 1. Automatické přejmenování původní složky
if os.path.exists(OLD_INPUT_DIR) and not os.path.exists(INPUT_DIR):
    os.rename(OLD_INPUT_DIR, INPUT_DIR)
    print(f"Složka '{OLD_INPUT_DIR}' byla automaticky přejmenována na '{INPUT_DIR}'.")
elif not os.path.exists(INPUT_DIR):
    print(f"CHYBA: Složka '{INPUT_DIR}' ani '{OLD_INPUT_DIR}' neexistuje.")
    exit(1)

# Vytvoření hlavní výstupní složky
Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

# Regulární výraz pro detekci abstraktu
ABSTRACT_PATTERN = re.compile(r'^\s*(ABSTRACT|ABSTRAKT)\b', re.IGNORECASE | re.MULTILINE)

def process_pdfs():
    input_path = Path(INPUT_DIR)
    output_path = Path(OUTPUT_DIR)
    
    # rglob("*.pdf") najde všechna PDF i uvnitř podsložek (vyvoj, test, validace)
    pdf_files = list(input_path.rglob("*.pdf"))
    
    if not pdf_files:
        print(f"Ve složce {INPUT_DIR} a jejích podsložkách nebyla nalezena žádná PDF.")
        return

    for pdf_file in pdf_files:
        # Získání relativní cesty (např. "vyvoj/soubor.pdf")
        rel_path = pdf_file.relative_to(input_path)
        # Sestavení cesty pro uložení (např. "stazene_prace_bez_abstraktu/vyvoj/soubor.pdf")
        out_file = output_path / rel_path
        
        # Zajištění, že existuje příslušná podsložka ve výstupním adresáři
        out_file.parent.mkdir(parents=True, exist_ok=True)
        
        print(f"\nZpracovávám: {rel_path}")
        
        try:
            reader = PdfReader(pdf_file)
            writer = PdfWriter()
            pages_removed = 0
            
            for page_num, page in enumerate(reader.pages):
                text = page.extract_text()
                
                if text:
                    # Prohledáváme jen prvních 1500 znaků, abychom nesmazali špatnou stranu
                    text_start = text[:1500]
                    if ABSTRACT_PATTERN.search(text_start):
                        print(f"  -> Nalezen abstrakt na straně {page_num + 1}. Stránku mažu.")
                        pages_removed += 1
                        continue
                
                writer.add_page(page)
            
            with open(out_file, "wb") as f:
                writer.write(f)
                
            if pages_removed == 0:
                print("  -> Žádný abstrakt nenalezen. Soubor zkopírován beze změny.")
                
        except Exception as e:
            print(f"  -> CHYBA při zpracování souboru {rel_path}: {e}")

if __name__ == "__main__":
    process_pdfs()
    print(f"\nHotovo! Původní práce jsou v '{INPUT_DIR}', upravené práce zachovaly strukturu v '{OUTPUT_DIR}'.")