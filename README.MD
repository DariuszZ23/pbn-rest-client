# 📚 PBN REST Client (Python)

Skrypt w Pythonie umożliwiający wyszukiwanie publikacji naukowych oraz autorów w systemie [[Polska Bibliografia Naukowa](https://pbn.nauka.gov.pl/)]  na podstawie zadanych kryteriów przez użytkownika.

---

## 🚀 Funkcjonalności

✅ Pobieranie danych z REST API PBN
✅ Wprowadzanie kryteriów wyszukiwania z konsoli (np. nazwisko lub imię lub fragment tytułu publikacji)
✅ Automatyczne rozdzielenie wyników na:

* 👤 osoby (autorzy)
* 📚 publikacje

✅ Czytelne wyświetlanie wyników w konsoli
✅ Obsługa podstawowych pól (imię, nazwisko, tytuł, DOI, rok)

---

## 🛠️ Wymagania

* Python 3.8+
* biblioteka `requests`

Instalacja:

```bash
pip install requests
```

---

## ▶️ Uruchomienie

```bash
python main.py
```

Po uruchomieniu program poprosi o podanie kryteriów:

```text 
kryterium nazwisko
Podaj kryteria wyszukiwania: zerynger

kryterium nazwa uczelni 
Podaj kryteria wyszukiwania: pjatk
```

---

## 📊 Przykładowy wynik dla kryterium nazwisko

```text
=== OSOBY ===
1. Piotr Zerynger Ośrodek Przetwarzania Informacji — Państwowy Instytut Badawczy (lic.)
2. Joanna Geringer-Grabda ()
3. Henryk Geringer de Oedenberg (prof. dr hab.)
4. Agnieszka Ceryngier Polsko-Japońska Akademia Technik Komputerowych (mgr inż.)
5. Piotr Ceryngier Uniwersytet Kardynała Stefana Wyszyńskiego w Warszawie (dr hab.)
6. Jakub Zenger Politechnika Poznańska (mgr inż.)

=== PUBLIKACJE ===
1. [1999] Beringer z Bambergu
   Typ: CHAPTER
2. [2014] Niedostrzegalni zabójcy: życie, różnorodność i znaczenie parazytoidów
   Typ: CHAPTER
3. [2014] Niedostrzegalni zabójcy: życie, różnorodność i znaczenie parazytoidów
   Typ: CHAPTER
4. [2015] Ecology of dormancy in ladybird beetles (Coleoptera: Coccinellidae)
   Typ: ARTICLE
```

---

## 🌐 Wykorzystywane API

### PBN REST API

Endpoint:

```
https://pbn.nauka.gov.pl/core/rest/search/main/extended/0/10/current=true
```

Parametry:

* `query` – kryterium wyszukiwania

---

## 🧠 Logika działania

1. Program prosi o kryteria od użytkownika (`input`)
2. Wysyła zapytanie HTTP do API PBN
3. Odbiera odpowiedź w formacie JSON
4. Przetwarza dane:

   * `PersonContainer` → lista osób
   * `PublicationContainer` → lista publikacji
5. Wyświetla wyniki w podziale na sekcje

---

## ⚠️ Ograniczenia

* Program nie obsługuje poprawnie publikacji z wieloma autorami (różne struktury JSON)
* Nie wszystkie publikacje zawierają DOI
* Wyniki są ograniczone do pierwszych 10 rekordów (zgodnie z API)

---

## 🔧 Możliwe rozszerzenia

* obsługa wielu autorów w publikacjach
* filtrowanie wyników (np. tylko publikacje)
* sortowanie (np. po roku)
* zapis wyników do pliku (CSV / JSON)
* integracja z API Crossref (pobieranie ORCID)
* interfejs CLI (menu wyboru)

---

## 📌 Cel projektu

Projekt edukacyjny pokazujący:

* pracę z REST API
* przetwarzanie danych JSON
* operacje na strukturach danych w Pythonie (dict, list)
* podstawy integracji systemów

---

## 👨‍💻 Autor

Projekt stworzony w celach nauki i rozwijania umiejętności pracy z API.
