
from crud import insert_tactic


T_TACTICS = {
    "Mirage": [
        ("Pistol round",
         "Szybki wjazd na B przez Apartamenty (Apps). Kupujecie 3x pancerz, 2x P250 i smoke/flash. Jeden gracz rzuca dymny z okna na samochód (Van). Cała drużyna wybiega po rzuceniu dwóch fleszy nad oknami. Dwóch graczy wbiega bezpośrednio na site, reszta czyści Short i Edwarda."),
        ("Eco round",
         "Rush A przez Rampę i Palace. Cała piątka kupuje Glocki i biegnie bez zatrzymywania. Jeden gracz w Palace czeka, aż rampa wyjdzie, po czym wychyla z góry strzelając w plecy graczom na Ticket i Default. Ignorujecie Connector, celujecie w plant."),
        ("Half buy",
         "Split Mid na B. Kupujecie MAC-10/Scout. Rzucacie standardowy smoke na Top Mid i Window z respa. Dwóch graczy idzie przez Underpass, trzech przez Mid na Short. Synchronicznie wbiegacie z Shorta i Appsów (jeden gracz lurkuje przez Apps), biorąc B w kleszcze."),
        ("Full buy",
         "Pełne wejście na A. 3 dymne rzucane z respa: na Ticket, CT i Jungle/Stairs. Dwa molotovy na Default i Sandwich. Dwóch graczy wychodzi z Palace, trzech z Rampy. Gracz z bombą plantuje pod Palace, by po podłożeniu uciec i grać na czas z daleka."),
        ("Full buy",
         "Późny split A przez Mid. Zaczynacie wolno, kontrolując mapę (Default 1-3-1). Zabieracie Mid rzucając smoke na Window i Connector. Po minucie rzucacie smoke na Short i wchodzicie trzema graczami przez Connector na A, podczas gdy dwóch wspiera was granatami i wchodzi z Rampy.")
    ],
    "Inferno": [
        ("Pistol round",
         "Skrót przez Drugi Mid do Apps. Wszyscy kupują Kevlar lub ulepszone pistolety. Biegniecie przez Second Mid pod mostem. Jeden gracz zostaje na schodach osłaniając plecy, czterech wbiega do Apps. Rzucacie flesza na Pit i synchronicznie wyskakujecie z balkonu na A."),
        ("Eco round",
         "Rush Mid na Arch. Kupujecie P250/Dual Berettas. Biegniecie ławą przez środek. Rzucacie jednego flesza za róg i wybiegacie wprost na pozycję Arch (A). Skracacie dystans, próbujecie zdobyć jedną długą broń od CT i zaplantować bombę lub wycofać się na bezpieczną pozycję."),
        ("Half buy",
         "Pułapka na Bananie i rotacja przez CT. Dwóch graczy z deaglami rzuca pop-flesze nad murem Banana, szukając wczesnego fraga na wpychającym CT. Następnie trzech graczy rotuje dołem Banana przez Mid prosto na CT Spawn, by oflankować drużynę CT na A."),
        ("Full buy",
         "Powolne przejęcie B z pełnym oporządzeniem. Rzucacie głęboki smoke na dół Banana na początku. Po 40 sekundach podchodzicie do Car, rzucacie molotovy na Bags i CT. Dymny na CT i Spools, a po dwóch fleszach nad dachem wbiegacie we dwóch na First Oranges, a jeden szuka fraga w ciemni (Dark)."),
        ("Full buy",
         "Wejście na A z Bracket (Mid). Przejmujecie Mid na początku, rzucając dymny na Arch. Trzech graczy idzie przez Short rzucając molotov na Pit i dymny na Moto (Bibliotekę). Dwóch graczy w tym czasie kontroluje Apps i wchodzi stamtąd, zamykając graczy z A w potrzasku krzyżowego ognia.")
    ],
    "Nuke": [
        ("Pistol round",
         "Rush Rampa do B. Wszyscy bez zatrzymywania kupują Kevlar i z Glockami wbiegają na Rampę. Jeden gracz rzuca dymny tuż przed wejściem. Wybiegacie z Rampa, jeden schodzi na dół po schodach, pozostali wpadają prosto na dolny bombsite B plantując pod drzwi."),
        ("Eco round",
         "Rush Outside do Secret. Cała drużyna biegnie Outside. Używacie tylko zbroi i Glocków, polegacie na sile grupy. Zbiegacie błyskawicznie po schodach do Secret, otwieracie drzwi Decon i próbujecie zalać B. Cel to rozbicie wrogiej ekonomii."),
        ("Half buy",
         "Wejście Squeaky z wpadnięciem do Vent. Kupujecie PM-y. Wyważacie drzwi Squeaky strzałem, rzucacie jednego dymnego między Main a Mini, a potem cała trójka rozwala Vent i natychmiast skacze na dół do B, podczas gdy dwóch graczy robi hałas na Rampie, myląc rotacje CT."),
        ("Full buy",
         "Pełna kontrola Outside i wejście Secret. Rzucacie linię dymnych ze spawnu (tzw. ściana na Outside) odgradzając Garage i Mini. Trzech graczy przebiega do Secret i wchodzi powoli na B, metodycznie czyszcząc kąty za pomocą fleszy (Dark, Toxic). Dwóch graczy łapie rotacje na Outside/Main."),
        ("Full buy",
         "Wejście A przez Hut i Squeaky. Rzucacie granaty HE na dach Hut (na pozycje pod dachem). Po rzuceniu dymnego z Lobby na Main, otwieracie Squeaky. Dwóch wychyla ze Squeaky po molotovie rzuconym na Hut, a trzech graczy wyskakuje z okien z Hut na site, celując w Rafters/Mini.")
    ],
    "Dust II": [
        ("Pistol round",
         "Szybki push na B przez Tunele. 3 graczy kupuje ulepszony pancerz (Kevlar). Dwóch graczy wspiera rzucając flesze nad Tunelem B. Cała drużyna wybiega synchronicznie bez zatrzymania prosto pod okno (Window), izolując przeciwników, żeby zaplantować przed wejściem rotacji z Mid."),
        ("Eco round",
         "Rush Długiej A (Long Doors). 5x Kevlar, szybkie kroki. Jeden gracz rzuca dymny z biegu na drzwi CT przy skrzynce. Biegniecie całą grupą ignorując strzały z Pit, skupiacie się na graczu na rogu dążąc do jak najszybszego podłożenia bomby."),
        ("Half buy",
         "Szybki atak przez Mid na B. Kupujecie Scout/Deagle. Jeden dymny ląduje w drzwiach Mid. Przebiegacie na B przez Mid i szparę w drzwiach do Window, rzucając pop-flash. Strzelcy z Deaglami celują w Window/Door na B, zmuszając pasywnych graczy CT do odsłonięcia się."),
        ("Full buy",
         "Split A przez Short i Long. Dwóch graczy trzyma Long, rzucając dymny na róg i przejmując Pit. Trzech graczy wychodzi powoli na Short po zrzuceniu dymnego z respa na X-Box. Synchroniczny wyjazd – Short rzuca flesze na Site, podczas gdy Long wybiega na Rampę."),
        ("Full buy",
         "Kontrola Short i ostateczne wejście B. Początkowo 3 graczy wychodzi na Short rzucając molotovy na Site A i dymny CT, markując wejście na A. W połowie rundy cicho wycofują się przez Mid do Lower Tunnels i uderzają na B całą pięcioosobową drużyną wspólnie z graczami z Upper.")
    ],
    "Ancient": [
        ("Pistol round",
         "Rush B przez Cave (Rampę B). Wszyscy wbiegają razem. Jeden z graczy rzuca smoke na wejście Cave. Na komendę wybiegacie rozpraszając się po całym Pillarze i plantując bombę od strony wody (Water), odcinając widok z CT."),
        ("Eco round",
         "Cicha wędrówka do Donut i zgniecenie Mid. Cała ekipa powoli zakrada się przez wodę do Donut, czekając tam bezgłośnie na pozycjach przez minutę. Gdy CT zacznie szukać graczy, wypadacie z Donut i Mid synchronicznie zdobywając mapę środkiem."),
        ("Half buy",
         "Szybki wjazd A Main z MAC-10. Bez ociągania wybiegacie przez A Main. Jeden rzuca błyskowego granata z biegu, cała reszta skacze na Default i CT, celując z bliska. Nawet jeśli was zbiją, szukacie chociaż dwóch zabójstw by nadszarpnąć ich portfele."),
        ("Full buy",
         "Split B przez Cave i Alley. Trzech graczy idzie do B Cave rzucając wczesne dymne na Cave-Mid. Dwóch idzie główną drogą do B (Alley). Rzucacie smoke'i na Short (Cave) i CT. Wyjazd następuje symultanicznie po podwójnym flashu nad murem od strony Alley."),
        ("Full buy",
         "Wyjazd A z odcięciem dymnym CT. Rzucacie 2 smoke z A Main na lewą i prawą stronę CT. Molotov na Temple i Default. Trzech graczy wbiega od A Main prosto do plantowania pod Main. Pozostałych dwóch wspiera z T-Spawn rzucając anty-rotacyjne dymne na Mid (Donut).")
    ],
    "Anubis": [
        ("Pistol round",
         "Szybki atak B Main. Wszyscy kupują Kevlar. Jeden rzuca pop-flash zza ściany przed wejściem i wychylacie z lewej i prawej strony Pillar. Gracz z bombą ucieka i chowa się na Backsite natychmiast po zaplantowaniu, by uniknąć odbicia przez CT z USP."),
        ("Eco round",
         "Flanka przez Wodę do Mida. Przebiegacie od razu do Wody z Glockami/P250, schodząc pod mostem. Jeśli woda jest pusta, wchodzicie przez podwójne drzwi na plecy na Mid, celując prosto w rotujących snajperów z A i B. Maksymalny chaos w środku mapy."),
        ("Half buy",
         "Agresja A Main. Pięciu graczy wjeżdża A Main z Tec-9 i MAC-10. Rzucacie jeden smoke na Drop / Camera, żeby odciąć wsparcie. Wybiegacie bardzo szeroko na Site A, nie przejmując się zgonami na wejściu. Skupiacie się na zdobyciu choć jednego M4 i szybkiego planta."),
        ("Full buy",
         "Standardowy split B z Midem. Dwóch graczy łapie powoli kontrolę nad Mid Bridge. Trzech podchodzi do B Main. Rzucacie dymny na CT i Connector z Mida, po czym wychylacie wejściem Main rzucając molotovy na Backsite. Gracz z Mida idzie flanką od strony wodnej na B."),
        ("Full buy",
         "Atak A z wyłączeniem Camera. Zrzucacie dymne na pozycje Heaven (CT) i na okno (Camera) ze spawnu. Wchodzicie całą piątką przez A Main z fleszami odbijanymi od filarów. Plantujecie bombę pod A Main na bezpiecznej flance i brronicie po rzuceniu zapalających w rotacje CT.")
    ],
    "Train": [
        ("Pistol round",
         "Zalanie Ivy i skrót A. Cała piątka wbiega do T-Main i pcha od razu przez Ivy (zielony korytarz). Z P250 i jednym smoke odcinacie CT w Ivy, po czym skracacie dystans wjeżdżając na tyły A (na Olof i Z) łapiąc obrońców Outer w kleszcze z całkowitego zaskoczenia."),
        ("Eco round",
         "Rush Upper B. Najszybsza taktyka, nie zwalniacie. Wszyscy z Kevlarami, biegną Upper Ramp w stronę B. Jeden rzuca z biegu pop-flash o prawą ścianę tunelu, by oślepić kryjącego za Z lub filarami. Wysypujecie się ze schodów i idziecie prosto w głowy z Glocków w walce w zwarciu."),
        ("Half buy",
         "Atak zeskoku Popdog. Ciche podejście 4 graczy z górnymi pozycjami do drabin Popdog z z SMG. 1 gracz na T Main rzuca dymny na Z. Odbijacie flesza o drabiny i zeskok w cztery osoby prosto pod A, celując na graczy ukrytych pod pociągami na bombsite."),
        ("Full buy",
         "Wejście Outer (A) pod ścianą dymną. Rzucacie klasyczną ścianę ze smoke'ów (3 sztuki od strony T Main na łącznik/Z i tył site'u). Czekacie na wybuchy mołotowów i wybiegacie na raz w 4 z Olof i 1 z Ivy. Plantujecie pod bombę w bezpiecznym rogu uciekając między zielone pociągi."),
        ("Full buy",
         "Późny split B przez Upper i Lower. Początek rundy poświęcony zbijaniu utilów przeciwnika na A z użyciem pojedynczych granatów. Po minucie dwóch wbiega cicho w Lower Ramp, trzech na Upper Ramp. Rzucają molotov na Spools (tyły). Górni fleszują, dolni wchodzą z osłoną dymu do samego centrum bombsite'u.")
    ]
}


def seed_t_tactics():
    print("Rozpoczynam wgrywanie 35 taktyk dla strony T...")
    side_name = "T"
    count = 0

    for map_name, tactics in T_TACTICS.items():
        for tactic in tactics:
            economy_name = tactic[0]
            description = tactic[1]
            insert_tactic(map_name, side_name, economy_name, description)
            count += 1

    print(f"Sukces! Wgrano {count} taktyk dla T do bazy danych.")


if __name__ == "__main__":
    seed_t_tactics()