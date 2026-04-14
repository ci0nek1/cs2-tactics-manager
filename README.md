# CS2 Strat Roulette Pro 🎮

**CS2 Strat Roulette Pro** to lekka, konsolowa aplikacja napisana w języku Python, służąca do losowania taktyk w grze Counter-Strike 2. Program pozwala graczom na wylosowanie konkretnego planu na rundę w zależności od wybranej mapy, strony (CT/T) oraz stanu ekonomii.

## 🌟 Główne funkcjonalności
* **Interaktywne menu konsolowe:** Prosty w obsłudze interfejs użytkownika z zabezpieczeniami przed wprowadzeniem błędnych danych (np. liter zamiast cyfr).
* **Obsługa bazy danych (SQLite):** Trwałe przechowywanie map, stron, stanów ekonomii oraz przypisanych do nich taktyk.
* **Inteligentne losowanie:** Algorytm dobierający losową taktykę z bazy danych na podstawie trzech filtrów jednocześnie (mapa, strona, ekonomia).

## 🛠 Wykorzystane technologie
* **Język:** Python 3.x
* **Baza danych:** SQLite (moduł `sqlite3`)
* **Testowanie:** `unittest`, `unittest.mock` (mockowanie wejścia/wyjścia i bazy danych)
* **Środowisko:** PyCharm / VS Code

## 📁 Struktura plików
* `main.py` - Logika menu i obsługa wejścia użytkownika.
* `crud.py` - Operacje na bazie danych (Create, Read).
* `database.py` - Konfiguracja połączenia z bazą SQLite.
* `test_main.py` - Testy jednostkowe interfejsu (mocki).
* `test_crud_temp_db.py` - Testy integracyjne bazy danych (tymczasowa baza w pamięci/pliku).
* `specyfikacja.md` - Szczegółowa dokumentacja projektowa.

## 🚀 Instrukcja instalacji i uruchomienia
1.  Upewnij się, że masz zainstalowanego **Pythona 3.x**.
2.  Sklonuj repozytorium:
    ```bash
    git clone [URL-TWOJEGO-REPOZYTORIUM]
    ```
3.  Przejdź do folderu projektu:
    ```bash
    cd cs2-tactics-manager
    ```
4.  Uruchom aplikację:
    ```bash
    python main.py
    ```

## 🧪 Testowanie
Projekt zawiera zestaw **7 zautomatyzowanych testów**, co spełnia wymóg minimum 5 testów jednostkowych.
* **Status testów:** ✅ Wszystkie testy przechodzą pomyślnie.

Aby uruchomić testy, użyj komend:
```bash
python -m unittest test_main.py
python -m unittest test_crud_temp_db.py
```

## 👨‍💻 Zrealizowane samodzielnie:
* **Koncepcja i architektura:** Wymyślenie zasad działania aplikacji, zaprojektowanie struktury danych oraz mechaniki filtrowania taktyk na podstawie 3 parametrów (mapa, strona, ekonomia).
* **Logika aplikacji:** Stworzenie głównej pętli sterującej programem w pliku `main.py` oraz interaktywnego menu konsolowego.
* **Operacje bazodanowe:** Zdefiniowanie struktury tabel dla bazy SQLite oraz napisanie podstawowych zapytań w pliku `crud.py` (funkcje Create i Read).
* **Kontrola wersji:** Obsługa repozytorium Git, tworzenie historii zmian (commitów) zgodnie z wytycznymi ("This commit will...").
* **Weryfikacja:** Ręczne testowanie manualne i kontrola poprawności działania programu na każdym etapie.

## 🤖 Zrealizowane przy wsparciu AI:
* **Automatyczne testy (Mockowanie):** AI pomogło w poprawnej implementacji biblioteki `unittest.mock`. Asystent wygenerował przykłady użycia dekoratorów `@patch`, co pozwoliło odizolować funkcję `input()` podczas testowania interfejsu.
* **Testy integracyjne:** Asystent zasugerował i pomógł napisać kod tworzący tymczasową bazę danych w pamięci (`setUp` i `tearDown` w `test_crud_temp_db.py`), co pozwoliło na bezpieczne testowanie zapytań SQL.
* **Dokumentacja i formatowanie:** AI wsparło proces redagowania plików tekstowych (`README.md`, `specyfikacja.md`), formatując je do czytelnego standardu Markdown oraz pomogło wygenerować polskojęzyczne komentarze (docstrings) w kodzie.
* **Refaktoryzacja zabezpieczeń:** Drobne poprawki optymalizacyjne, takie jak zabezpieczenie wprowadzania danych przez użytkownika za pomocą bloków `try-except` (wylapywanie bledu `ValueError`).
* 