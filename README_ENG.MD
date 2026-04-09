# 📚 PBN REST Client (Python)

Python script for searching scientific publications and authors in the Polish Scientific Bibliography system based on user-defined search criteria.

---

## 🚀 Features

✅ Retrieving data from the PBN REST API
✅ Entering search criteria from the console (e.g. surname, first name, or part of a publication title)
✅ Automatic separation of results into:

* 👤 people (authors)
* 📚 publications

✅ Clear display of results in the console
✅ Support for basic fields (name, surname, title, DOI, year)

---

## 🛠️ Requirements

* Python 3.8+
* `requests` library

Installation:

```bash id="k3rjlwm"
pip install requests
```

---

## ▶️ Running the Program

```bash id="ytlhm9"
python main.py
```

After launching, the program will ask for search criteria:

```text id="5wwa9r"
criterion: surname
Enter search criteria: zerynger

criterion: university name
Enter search criteria: pjatk
```

---

## 📊 Example Output for the Surname Criterion

```text id="y0hnm7"
=== PEOPLE ===
1. Piotr Zerynger Ośrodek Przetwarzania Informacji — Państwowy Instytut Badawczy (lic.)
2. Joanna Geringer-Grabda ()
3. Henryk Geringer de Oedenberg (prof. dr hab.)
4. Agnieszka Ceryngier Polsko-Japońska Akademia Technik Komputerowych (mgr inż.)
5. Piotr Ceryngier Uniwersytet Kardynała Stefana Wyszyńskiego w Warszawie (dr hab.)
6. Jakub Zenger Politechnika Poznańska (mgr inż.)

=== PUBLICATIONS ===
1. [1999] Beringer z Bambergu
   Type: CHAPTER
2. [2014] Niedostrzegalni zabójcy: życie, różnorodność i znaczenie parazytoidów
   Type: CHAPTER
3. [2014] Niedostrzegalni zabójcy: życie, różnorodność i znaczenie parazytoidów
   Type: CHAPTER
4. [2015] Ecology of dormancy in ladybird beetles (Coleoptera: Coccinellidae)
   Type: ARTICLE
```

---

## 🌐 Used API

### PBN REST API

Endpoint:

```text id="2gv4n7"
https://pbn.nauka.gov.pl/core/rest/search/main/extended/0/10/current=true
```

Parameters:

* `query` – search criterion

---

## 🧠 How It Works

1. The program asks the user for search criteria (`input`)

2. Sends an HTTP request to the PBN API

3. Receives the response in JSON format

4. Processes the data:

   * `PersonContainer` → list of people
   * `PublicationContainer` → list of publications

5. Displays the results divided into sections

---

## ⚠️ Limitations

* The program does not correctly support publications with multiple authors (different JSON structures)
* Not all publications contain a DOI
* Results are limited to the first 10 records (according to the API)

---

## 🔧 Possible Extensions

* support for multiple authors in publications
* filtering results (e.g. only publications)
* sorting (e.g. by year)
* saving results to a file (CSV / JSON)
* integration with the Crossref API (retrieving ORCID)
* CLI interface (selection menu)

---

## 📌 Project Goal

Educational project demonstrating:

* working with REST APIs
* processing JSON data
* operations on Python data structures (`dict`, `list`)
* basics of system integration

---

## 👨‍💻 Author

Dariusz Zerynger

Project created for learning purposes and developing API integration skills.
