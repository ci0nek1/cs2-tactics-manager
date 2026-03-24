# seed_ct.py
from crud import insert_tactic

# Struktura: { "Nazwa Mapy": [ ("Ekonomia", "Opis taktyki"), ... ] }
CT_TACTICS = {
    "Mirage": [
        ("Pistol round",
         "Ustawienie 2-1-2. Dwóch graczy na B gra crossfire z Van i Short. Jeden gracz na Window (gra pasywnie, zbiera info). Dwóch graczy na A - jeden Ticket, jeden Default. Na B trzymajcie smoke na aplikacje (Apps), na wypadek agresywnego wjazdu."),
        ("Eco round",
         "Agresywny push 5 na Rampę (A). Kupujecie P250 i jeden dymny. Rzucacie smoke na Tetris, błyskacie nad Rampą i wchodzicie skrótem do T-Spawn, aby zdobyć bronie. Jeśli zdobędziecie AK/Galil, rotujcie z nim bezpiecznie z powrotem na CT."),
        ("Half buy",
         "Szybka kontrola Mid. Kupujecie 3x Scout, 2x Deagle. Jeden gracz puszcza smoke na Window (od wewnątrz) i dropi do Underpass z Deaglem. Dwóch ze Scoutami pushuje Shorta z fleszami. Szukacie szybkich fragów i wycofujecie się na bombsite'y."),
        ("Full buy",
         "Standardowe 2-1-2 z silną kontrolą Mid. Gracz Window gra z AWP. Gracz Connector gra agresywnie z M4 i rzuca wczesny molotov na Top Mid. Gracz z Shorta wspiera Window fleszami. Gracze na A i B grają z głębokich pozycji (Ticket / Backsite B)."),
        ("Full buy",
         "Retake setup na A. Trzech graczy silnie broni B i Mid (B Apps, Short, Window). Tylko dwóch graczy na A - grają z Ticket Booth i CT Spawn, całkowicie ukryci. Oddają bombsite A w przypadku wjazdu i czekają na rotację reszty z utilitami (flesze nad CT) do odbijania.")
    ],
    "Inferno": [
        ("Pistol round",
         "Ustawienie 3 na B, 2 na A. Na B jeden gracz kupuje defuse kit i gra głęboko za Sandbags. Dwóch gra z CT/Coffins. Na A gracze trzymają Pit i Short z krzyżowym ogniem. Zero agresji, czekacie cierpliwie na wejście w strefę strzału."),
        ("Eco round",
         "Agresja na Banana. Cała piątka rzuca podwójnego flesza nad dachem na B i synchronicznie wbiega na Bananę. Próbujecie odizolować i zabić graczy robiących kontrolę banana, zabrać im broń i zrotować bezpiecznie przez Mid na A."),
        ("Half buy",
         "Pułapka w Apartamentach (Apps). 3 graczy z MP9/Shotgunami siedzi w Boilerze i na górze Appsów na A. Gdy T wejdą, robicie szybki atak z bliska w ciasnym przejściu. B bronią 2 osoby z Deaglami grające zachowawczo na szybki retake z CT."),
        ("Full buy",
         "Klasyczne 3 na A, 2 na B. Na B ciągła presja na Bananie: rzucacie wczesny molotov na Car (Bags), następnie głęboki smoke na dół Banana. Na A jeden Pit, jeden Balcony, jeden na Arch przygotowany do szybkiej rotacji na B w razie potrzeby."),
        ("Full buy",
         "Stack na A. 4 graczy mocno broni A (Arch, Pit, Graveyard, Short). Tylko jeden gracz gra na B solo z AWP na CT, zbierając jedynie info. Jeśli T idą na B, gracz z AWP się natychmiast cofa do Ruins i czeka na całą drużynę do odbijania B.")
    ],
    "Nuke": [
        ("Pistol round",
         "Pasywny crossfire na Upper (A). Dwóch na Hut (jeden na dachu Squeaky, drugi na Rafters). Jeden broni Main. Jeden schodzi od razu na Ramp, a jeden gra Outside z USP-S wykorzystując przewagę dystansu pistoletów CT."),
        ("Eco round",
         "Rush Squeaky. Otwieracie drzwi i cała piątka wbiega na Lobby z P250, rzucając wcześniej jednego flesza przez uchylone drzwi. Cel to zaskoczyć T przygotowujących się do powolnego ataku na Outside lub Rampę."),
        ("Half buy",
         "Agresywny Outside. 4 graczy z pistoletami maszynowymi (MAC-10/MP9) przebiega do Red Boxa od razu przy użyciu pierwszego smoke'a. Jeden snajper ze Scoutem gra na Garage, osłaniając ich plecy i szukając obić."),
        ("Full buy",
         "Zbalansowana obrona 1-2-1-1. Jeden gracz gra Vents, reagując na dźwięki ze Squeaky. Dwóch graczy na Outside (jeden Secret, jeden Garage/Mini). Jeden na Ramp z AWP grający kąty, a ostatni gracz asekuruje Heaven na A."),
        ("Full buy",
         "Obrona Dolnego poziomu (B). Odpuszczacie całkowicie Upper A na starcie. 2 graczy broni Rampy z głębokich pozycji. 3 graczy schodzi na dół (Secret, Vents, Decon) i budują żelazną obronę (krzyżowy ogień z Drzwi na B i Dark/Toxic).")
    ],
    "Dust II": [
        ("Pistol round",
         "Standardowe 2-1-2. Dwóch graczy blokuje B z pozycji Window i Door (krzyżowo). Jeden patrzy na Mid z CT Spawn. Dwóch wchodzi na A Long - rzucają granat HE od razu na drzwi i schodzą do Pit grając bezpieczny crossfire z dystansu."),
        ("Eco round",
         "Pułapka Lower Tunnels. Cała piątka wbiega od razu z B przez podwójne Doors do Lower Tunnels. Czekacie cicho w rogu schodów. Gdy tylko T wejdą z górnego trupa lub wyjdą z Mid, wychyłacie wszyscy na raz strzelając w plecy."),
        ("Half buy",
         "Szybki skrót na Catwalk (Short). 3 graczy z Deaglami i jednym Scoutem wbiega na Short, rzuca pop-flesza nad ceglanym murem i wychyla na Top Mid szukając otwarcia. Dwóch pozostałych broni B pasywnie z Back Plat i ukrywa się."),
        ("Full buy",
         "Pełna kontrola Longa. 3 graczy z pełnym granatami rusza na A Long, rzucając smoke na róg i molotov w stronę niebieskich drzwi T. Cel to wczesne zdobycie Pit i Car. 1 gracz zbiera info na Mid, 1 trzyma B defensywnie z pozycji Window."),
        ("Full buy",
         "Stack na B. 3 graczy murowanie trzyma B (Window, Backsite, Car) z dużą ilością granatów zapalających do opóźniania. 2 graczy na A gra retake setup z CT Spawn i Ramp, odpuszczając kompletnie Longa na początku rundy na rzecz obrony AWP.")
    ],
    "Ancient": [
        ("Pistol round",
         "Ustawienie 2 na A Main, 1 na Mid, 2 na B Ramp. Na B gracze zajmują bardzo bliskie pozycje w Cave, czekając na szybki wjazd. Na A gracze grają zza Default i CT, używając celności USP-S do headshotów na średni dystans."),
        ("Eco round",
         "Agresja na Mid z Donut. Wszyscy kupują P250. 3 wchodzi błyskawicznie do Donut, 2 na Mid od strony CT. Rzucacie flesza w stronę drzwi (Red) i wychyłacie synchronicznie, by zdobyć map control i zabić rozstawiających się graczy."),
        ("Half buy",
         "Zamknięcie Cave (B). 4 graczy kupuje strzelby (MAG-7) i MP9, po czym stakuje się wokół wejścia do Cave na B. Rzucają jeden smoke by zmusić T do przejścia w ciemno. Czekają w bardzo bliskich kontaktach, 1 gracz osłania A grając ukryty na CT."),
        ("Full buy",
         "Dominacja Mid. 3 graczy bezwzględnie zajmuje Mid z głębokimi smoke'ami (na T-Mid i Xbox), zmuszając T do gry na zewnątrz. Odbierają T miejsce do manewru. 1 gracz samotnie broni B z Cave (grając zachowawczo), 1 samotnie trzyma A wycofany na Donut."),
        ("Full buy",
         "Pasywny Mid i Stack A. Oddajecie Mid na początku rundy. 3 graczy stakuje się wokół A Main i Donut broniąc bomb-site'u. 2 graczy ustawia się na B w okolicach Pillar, używając cyklicznych smoke'ów, by opóźnić jakikolwiek atak. Retake Mida robicie tylko na info.")
    ],
    "Anubis": [
        ("Pistol round",
         "Setup 2 B, 1 Mid, 2 A. Na Midzie (Bridge) gracz rzuca HE w stronę podwójnych drzwi i cofa za filar. Na A gracze grają z głębi site'u (blisko Heaven i Camera). Na B crossfire z Backsite i Pillar z użyciem USP-S."),
        ("Eco round",
         "Skrót przez Wodę (Canals). Cała drużyna biegnie schodami z Mid bezpośrednio do Wody z ulepszonymi pistoletami, rzucając pop-flasha o ścianę. Próbujecie wyczyścić Wodę z ewentualnych lurkerów i oflankować T pod ich spawnem."),
        ("Half buy",
         "Push A Main. 3 graczy z PM-ami (MAC-10/MP9) wybiega błyskawicznie przez A Main w stronę spawn T, rzucając wczesny flash i smoke na schody od strony T, by zająć plac na zewnątrz. Dwóch graczy na B i Mid gra ultra-defensywnie na info."),
        ("Full buy",
         "Standardowe 2-1-2 z silnym opóźnianiem B. Na B rzucacie ciągłe, głębokie smoke'i na B Main i molotovy w wejście, grając zza murku. Mid broniony pasywnie przez snajpera z Connector. Na A agresywna gra snajpera/riflera szukającego pierwszego fraga z Drop/Camera."),
        ("Full buy",
         "Mid stack z pułapką Wodną. 3 graczy z silną bronią we wczesnej fazie rundy zajmuje Mid i Wodę (Canals), skutecznie odcinając T od szybkiej rotacji. Po zdobyciu przewagi rozstawiają się szeroko. A i B obstawione przez pojedynczych graczy grających z głębi site'ów na retake.")
    ],
    "Train": [
        ("Pistol round",
         "Ustawienie 3 na Outer (A), 2 na Inner (B). Na Outer: jeden gra Popdog (Ladder), jeden na długim dystansie w Ivy z USP, jeden na Z/Connector. Inner to mocny krzyżowy ogień z Upper Ramp i Lower Ramp z użyciem pancerzy bez hełmu."),
        ("Eco round",
         "Rzeź w Ivy. Wszyscy kupują P250/Dual Berettas. 5 graczy w trybie cichym biegnie pod Ivy, na komendę rzucają dwa flesze za róg i wbiegają na pełnej szybkości w stronę wózka T, skracając dystans i wymuszając chaotyczną walkę z zaskoczenia."),
        ("Half buy",
         "Pułapka w Popdog (Ladder Room). 4 graczy zdejmuje buty i chowa się po kątach wokół drabin i w korytarzu Popdog z SMG i Deaglami. Jeśli T spróbują przejąć kontrolę nad drabinami, wejdą w masowy ogień z bliska. Jeden gracz obserwuje B z Backsite."),
        ("Full buy",
         "Kontrola Outer (A). 3 graczy na zewnątrz, z czego jeden ma AWP i gra agresywnie na Main (Olof) zbierając wczesne info. Gracz w Ivy gra głęboko, by uniemożliwić oflankowanie. 2 graczy broni Inner (B) grając w ścisłym duecie pomiędzy pociągami w razie wjazdu z Upper."),
        ("Full buy",
         "Stack na Inner (B). 4 graczy schodzi na bombsite B we wczesnej fazie rundy, blokując Upper i Lower potężnym crossfire'em z Z, Backsite i zza pociągów z użyciem molotovów. Na A (Outer) zostaje tylko jeden snajper (np. na Green/CT Train) by zebrać info, rzucić dymny i uciec.")
    ]
}


def seed_ct_tactics():
    print("Rozpoczynam wgrywanie 35 taktyk dla strony CT...")
    side_name = "CT"
    count = 0

    for map_name, tactics in CT_TACTICS.items():
        for tactic in tactics:
            economy_name = tactic[0]
            description = tactic[1]
            insert_tactic(map_name, side_name, economy_name, description)
            count += 1

    print(f"Sukces! Wgrano {count} taktyk dla CT do bazy danych.")


if __name__ == "__main__":
    seed_ct_tactics()