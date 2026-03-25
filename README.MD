# 📚 PBN REST Client (Python)

Prosty program w Pythonie umożliwiający wyszukiwanie publikacji naukowych oraz autorów w systemie PBN (Polska Bibliografia Naukowa) na podstawie nazwiska podanego przez użytkownika.

---

## 🚀 Funkcjonalności

✅ Pobieranie danych z REST API PBN
✅ Wprowadzanie nazwiska autora z konsoli
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
Podaj kryteria wyszukiwania: robert
```

---

## 📊 Przykładowy wynik

```text
=== OSOBY ===
1. Robert Miotk Instytut Maszyn Przepływowych im. Roberta Szewalskiego Polskiej Akademii Nauk (dr)
2. Robert Barbucha Instytut Maszyn Przepływowych im. Roberta Szewalskiego Polskiej Akademii Nauk (dr inż.)
3. Robert Matysko Instytut Maszyn Przepływowych im. Roberta Szewalskiego Polskiej Akademii Nauk (dr hab. inż.)

=== PUBLIKACJE ===
1. [2018] Roberta Lockiego internalizm deontologiczny
   Typ: ARTICLE
2. [2018] Roberta Lockiego internalizm deontologiczny
   Typ: ARTICLE
3. [2019] Inferencjalizm semantyczny Roberta B. Brandoma
   Typ: BOOK
4. [2009] "Powrót historii" w ujęciu Roberta Kagana
   Typ: CHAPTER
5. [2005] Relacje transatlantyckie w kontekście rozważań Roberta Kagana,
   Typ: BOOK
6. [2016] R. C. Roberts, Emotions in the Moral Life
   Typ: ARTICLE
7. [2024] Transcendentalne argumenty Roberta Lockiego przeciw determinizmowi
   Typ: ARTICLE
   DOI: 10.18290/rf24722.22
```

---

## 🌐 Wykorzystywane API

### PBN REST API

Endpoint:

```
https://pbn.nauka.gov.pl/core/rest/search/main/extended/0/10/current=true
```

Parametry:

* `query` – nazwisko autora

---

## 🧠 Logika działania

1. Program pobiera nazwisko od użytkownika (`input`)
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
