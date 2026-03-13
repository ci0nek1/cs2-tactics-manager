# Specyfikacja projektu: CS2 Tactics Manager

## 1. Opis funkcjonalności
Aplikacja konsolowa służąca do zarządzania i losowania taktyk oraz rzutów granatów w grze Counter-Strike 2. Program rozwiązuje problem braku pomysłu na rundę, oferując doradztwo taktyczne na podstawie aktualnej sytuacji w meczu, a dane przechowywane są w nierelacyjnej bazie danych MongoDB.

**Główne funkcje aplikacji:**
* **Menu Główne:** Prosty interfejs tekstowy pozwalający użytkownikowi na nawigację po programie za pomocą klawiatury numerycznej.
* **Doradca Taktyczny (Losowanie taktyk):** Użytkownik podaje mapę, stronę (CT/T) oraz stan swojej ekonomii (Pistol, Eco, Force, Full). Program odpytuje bazę danych i losuje odpowiednią taktykę dla całej drużyny. Jeśli wylosowana taktyka nie odpowiada graczom, można wcisnąć klawisz 'R', aby natychmiast wylosować inną.
* **Baza Granatów:** Przeglądanie specyficznych rzutów (Smoke, Flash, Molotov) dla wybranej mapy. Program wyświetla listę dostępnych granatów wraz z linkami do zewnętrznych materiałów (np. zrzutów ekranu z punktem celowania).
* **Zarządzanie Bazą (Dodawanie wpisów):** Możliwość dodania nowej taktyki lub granatu bezpośrednio z poziomu konsoli. Dane są automatycznie formatowane, otrzymują unikalne ID i są trwale zapisywane w kolekcji MongoDB.

## 2. Wygląd aplikacji
Aplikacja opiera się na interfejsie tekstowym (CLI). Nawigacja odbywa się za pomocą wprowadzania odpowiednich wartości z klawiatury.

**Ekran Głównego Menu:**
```text
=== CS2 TACTICS MANAGER ===
1. Doradca Taktyczny
2. Baza Granatów
3. Dodaj nową taktykę
4. Wyjście
Wybierz opcję: _