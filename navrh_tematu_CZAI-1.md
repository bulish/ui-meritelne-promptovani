# První návrh tématu: Sumarizace odborných článků a porovnání s autorskými abstrakty

**Tým:** Libuše Babičková, Jakub Procházka (xproch40), Jan Kostrhun  

## 01 Výzkumná otázka

Jak se u systémů ChatGPT, Gemini, Claude a Perplexity liší sémantická shoda sumarizací odborných článků spojených s MENDELU s jejich autorskými abstrakty, měřená pomocí BERTScore F1, a do jaké míry ji zlepší strukturovaný a optimalizovaný prompt oproti společnému výchozímu promptu?

Zkoumáme schopnost vytvořit z textu článku stručné shrnutí cíle, metod, hlavních výsledků a závěrů. Výsledky pomohou při prvotní orientaci v odborné literatuře. Autorský abstrakt použijeme jako referenci; věrnost shrnutí vůči samotnému článku ověříme samostatně. Abstrakt nemusí zachycovat všechny důležité informace článku.

## 02 Hypotézy

**Hlavní hypotéza H1:** Za podmínek stejného vstupu bez abstraktu, společného protokolu webové práce se zdroji a stejného požadavku na délku dosáhne strukturovaný prompt vyššího průměrného BERTScore F1 než výchozí prompt napříč hodnocenými systémy, protože výslovně zaměřuje shrnutí na cíl, metody, výsledky a závěry. Hypotézu budeme považovat za podpořenou pouze tehdy, pokud se kladný párový rozdíl projeví také na deseti případech testovací sady držené stranou a jeho 95% bootstrapový interval bude celý nad nulou.

**Doplňková hypotéza H2:** Za stejných podmínek dosáhne optimalizovaný prompt vyššího průměrného BERTScore F1 než strukturovaný prompt, protože odstraní opakující se chyby identifikované na vývojových a validačních datech. Podporu posoudíme stejným pravidlem na testovací sadě.

**Alternativní vysvětlení:** Vyšší skóre může vzniknout větší podobností slovní zásoby a stylu s abstraktem, případně zapamatováním veřejně dostupného článku, aniž by se zlepšila faktická správnost. Proto změny BERTScore porovnáme s lidským hodnocením a SummaC. Hypotézy zpochybní nulový či záporný rozdíl na testovací sadě; interval zahrnující nulu znamená neprůkazný výsledek. Zhoršení věrnosti omezí praktickou interpretaci i při vyšším BERTScore.

## 03 Schopnosti a zaměření

Zvolíme **směr B: Výzkum podložený zdroji** a schopnost sumarizace odborného článku podložené ověřitelnými odkazy na jeho obsah. Jednotkou úlohy je jeden článek; jednotkou měření je výstup konkrétního systému v konkrétní podmínce promptu a opakování.

Výstup bude souvislé shrnutí v angličtině o 150–200 slovech, zahrnující informace dostupné v článku. Pracovní návrh počítá s anglickými články a abstrakty, aby se neměřil současně překlad a aby bylo možné využít anglický hodnoticí model SummaC. Závěry omezíme na tento korpus a zaznamenané verze produktů.

## 04 Systémy a nástroje

Budeme porovnávat **ChatGPT, Gemini, Claude a Perplexity**. Dostupnost webových funkcí a přístupu ke zdrojům ověříme v pilotu. Konkrétní modely a rozhraní zaznamenáme při sběru dat.

Použijeme návrh podle schopností produktu: každý systém využije své běžné webové nástroje podle společného protokolu. Dostane stejný text bez abstraktu a odkaz na původní článek; smí ověřovat tvrzení pouze v tomto zdroji, nesmí využít abstrakt ani jiné sumarizace. Každý běh začne v nové konverzaci a bude mít jedno uživatelské zadání. Paměť vypneme, kde je to možné. Výsledek interpretujeme jako porovnání produktů včetně vyhledávání, nikoli jako izolované schopnosti modelů. Metriky vypočítáme samostatným skriptem.

Porovnáme tři podmínky:

1. **Výchozí prompt:** „Summarize the following scientific article in English in 150–200 words. Use the supplied article and its linked full text only; do not use its abstract or other summaries. After the summary, list source sections supporting your main claims.“
2. **Strukturovaný prompt:** Stejný vstup a délka, navíc požadavek vystihnout cíl, metody, hlavní výsledky a závěry, zachovat čísla a odborné termíny, neopírat se o externí znalosti a nevymýšlet chybějící informace a doložit hlavní tvrzení odkazem na sekci či pasáž článku.
3. **Optimalizovaný prompt:** Úprava strukturované verze pouze podle vývojové a validační sady; zaznamenáme změny a zmrazíme jednu společnou verzi před otevřením testovací sady.

U běhů uložíme produkt, viditelný model, rozhraní, datum, verzi promptu a vstupu, dostupné systémové instrukce, nástroje, teplotu a výstupní limit, počet kol a volání nástrojů, latenci, náklady, selhání, opakování a zásahy člověka. Nedostupné údaje označíme.

## 05 Plán datasetu

Dataset bude obsahovat **40 odborných článků spojených s MENDELU**, s ověřeným oprávněním ke sdílení.

| Sada | Počet článků | Účel |
| --- | ---: | --- |
| Vývojová | 20 | Ladění promptů, přípravy vstupů a hodnocení |
| Validační | 10 | Výběr z nejvýše tří kandidátů optimalizovaného promptu |
| Testovací držená stranou | 10 | Jednorázové závěrečné vyhodnocení zmrazeného protokolu |

Výběr a rozdělení stratifikujeme podle oboru, délky a obtížnosti. Nejméně **8 článků (20 %)** bude představovat realistické okrajové případy: dlouhý kontext, vzácnou terminologii, složitá kvantitativní zjištění nebo nejednoznačné závěry. Rozdělíme je v poměru 4/2/2 mezi sady. Duplicitní a téměř shodné publikace odstraníme.

Z dodaného textu odstraníme abstrakt, jeho překlady, autorská shrnutí, kontaktní údaje a seznam literatury; zachováme odborný obsah včetně potřebných popisků a tabulek v jednotné textové podobě. Abstrakt uložíme odděleně jako referenci. Články musí po úpravě vyhovět společnému kontextovému limitu, bez dodatečného zkracování podle systému.

Každý případ bude mít ID, schopnost, typ úlohy, obtížnost, jazyk, příslušnost k sadě, prompt, vstup, očekávané vlastnosti, referenci, typ okrajového případu, způsob hodnocení a původ dat. Testovací obsah nepoužijeme k ladění. Pilot provedeme na třech vývojových článcích.

## 06 Metriky

| Metrika | Postavení | Co porovnává a měří |
| --- | --- | --- |
| BERTScore F1 | Hlavní, automatická | Sumarizaci s abstraktem; sémantickou podobnost pomocí kontextových reprezentací tokenů |
| SummaC-Conv | Vedlejší, automatická | Sumarizaci se vstupním článkem; odhad faktické konzistence pomocí rozpoznávání vztahů mezi tvrzeními |
| ROUGE-L F1 | Vedlejší, automatická | Sumarizaci s abstraktem; lexikální podobnost založenou na nejdelší společné podposloupnosti |

Na vývojové sadě ověříme funkčnost metrik a před testováním zmrazíme modely, verze knihoven, tokenizaci, segmentaci a nastavení skórování. BERTScore neprokazuje pravdivost, ROUGE-L penalizuje parafráze a SummaC může chybovat u odborných formulací a čísel.

Automaticky zkontrolujeme neprázdnost, délku a úplnost vloženého vstupu. Metriky vypočítáme jen ze shrnutí, bez následného seznamu zdrojových pasáží. Skóre uvedeme pro každý systém a prompt zvlášť; hlavní efekt promptu bude průměr párových rozdílů s rovnou vahou systémů. Nejistotu odhadneme párovým bootstrapem přes články, který zachová jejich související výstupy. Výsledky sad nebudeme slučovat do závěrečného testovacího skóre.

## 07 Lidské hodnocení

Členové týmu zhodnotí všechny závěrečné testovací výstupy, včetně plánovaných opakování. Alespoň 20 % výstupů posoudí nezávisle dva hodnotitelé. Identitu systému a podmínku promptu skryjeme a pořadí náhodně promícháme; hodnotitelé dostanou článek i abstrakt.

Rubrika bude hodnotit věrnost článku, pokrytí klíčových informací a správnost doložení tvrzení zdrojem na škále 1–5. Kotvy: **1** = zásadní zkreslení či chybějící klíčové informace; **3** = použitelné shrnutí s dílčími nedostatky; **5** = přesné, úplné a správně doložené shrnutí. Příklady vytvoříme na vývojové sadě. Shodu vyjádříme váženou Cohenovou kappou pro každou dimenzi. Neshody projdeme po nezávislém hodnocení s třetím členem; původní skóre zachováme. LLM nebude samostatným hodnotitelem. Analyzujeme nejméně osm reprezentativních případů včetně úspěchů a selhání.

## 08 Rušivé proměnné

Očekáváme vliv délky a oboru článku, kvality abstraktu, extrakce textu, délky výstupu, znalosti článku z tréninku, náhodnosti generování, webového vyhledávání, dostupnosti plného textu, kontextových limitů a změn produktů. Přístup k abstraktu přes web představuje riziko úniku reference; zaznamenáme viditelné zdroje a případné porušení protokolu, úplné vyloučení tohoto rizika nelze zaručit. Omezíme jej jednotným vstupem, délkou, stratifikací, krátkým sběrným obdobím a střídáním pořadí systémů. Zbytková omezení popíšeme.

Na dvou předem vybraných testovacích článcích provedeme druhý nezávislý běh každé kombinace systému a promptu. Neúspěchy zachováme, rozlišíme jejich příčinu a nebudeme je nahrazovat lepší odpovědí. Neplánovaná opakování nepovolíme. U neprázdných výstupů spočítáme metriky i při porušení délky; chybějící shrnutí označíme jako selhání a vedle skóre dostupných výstupů zveřejníme jejich počet a úspěšnost.

## 09 Ochrana dat

Použijeme jen články s licencí či výslovným oprávněním umožňujícím zamýšlené zpracování a sdílení se třídou; samotná veřejná dostupnost nestačí. Zaznamenáme zdroj, licenci a provedené úpravy. Nepoužijeme důvěrné materiály, osobní údaje účastníků výzkumu ani přístupové údaje. Z dodaného textu odstraníme kontaktní údaje; veřejné bibliografické údaje použijeme pouze k identifikaci zdroje. Data a výstupy uložíme do sdílené složky s přístupem týmu a vyučujícího; reference a testovací sadu oddělíme od vývojových podkladů.

## 10 Pracovní zátěž

Základní rozsah je **40 článků × 4 systémy × 3 prompty = 480 výstupů**, plus **24 opakovaných výstupů**. Z toho závěrečná testovací část obsahuje 144 výstupů včetně opakování; nejméně 29 projde dvojím hodnocením.

| Činnost | Odhad týmových hodin |
| --- | ---: |
| Výběr článků, licence, čištění a rozdělení dat | 4 |
| Pilot, prompty a hodnoticí skripty | 4 |
| Sběr výstupů a metadata | 4 |
| Lidské hodnocení a řešení neshod | 8 |
| Analýza, zpráva a reprodukovatelný balíček | 4 |
| **Celkem** | **24** |

Cílem je dokončit projekt do **25 hodin práce za celý tým**: 24 hodin plánovaných činností a 1 hodina rezervy, přibližně 8 hodin na osobu. Odhad předpokládá dávkové zpracování dat a metrik, automatizovaný sběr, nejvýše tři kandidátní prompty a stručné hodnocení s připravenými zdrojovými pasážemi. Proveditelnost ověříme v pilotu; čekání na odpovědi se nezapočítává do aktivní práce. Navržené hlavní role: Libuše Babičková koordinace datasetu a lidského hodnocení; Jakub Procházka (xproch40) prompty a sběr běhů; Jan Kostrhun metriky a analýza. Všichni se zapojí do hodnocení a zprávy. Náklady a čas budeme sledovat odděleně od kvality. Odevzdáme protokol, data, verze promptů, metadata, hodnoticí postupy, výsledky s nejistotou, analýzu chyb a závěrečnou zprávu.
