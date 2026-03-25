# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
# Jeśli publikacja ma wielu autorów to struktura JSON'a jest inna i nie jest obsługiwana.
def get_publication_by_surname(name):
    # pobranie frazy od użytkownika
    print("Pobiera publikacje według nazwiska autora z systemu 'Polskie Publikacje Naukowe'.")
    query = input("Podaj nazwisko autora: ")

    # URL endpointu
    url = "https://pbn.nauka.gov.pl/core/rest/search/main/extended/0/10/current=true&"

    # parametry zapytania
    params = {
        "query": query
    }

    # wykonanie requesta
    response = requests.get(url, params=params)

    # sprawdzenie statusu
    if response.status_code == 200:
        respJSON = response.json()

        persons = []
        publications = []

        for item in respJSON["data"]:
            if item["type"] == "PersonContainer":
                persons.append(item["data"])
                # print(item["data"]["qualifications"])
            elif item["type"] == "PublicationContainer":
                publications.append(item["data"])

        print("\n=== OSOBY ===")
        for idx, person in enumerate(persons[:], 1):
            name = person.get("nameAndEmployment", "Brak danych")
            qual = person.get("qualifications", "")
            print(f"{idx}. {name} ({qual})")

        print("\n=== PUBLIKACJE ===")
        for idx, pub in enumerate(publications[:], 1):
            title = pub.get("title", "Brak tytułu")
            year = int(pub.get("year", 0))
            ptype = pub.get("publicationType", "")
            doi = pub.get("doi", "")

            print(f"{idx}. [{year}] {title}")
            print(f"   Typ: {ptype}")
            if doi:
                print(f"   DOI: {doi}")

    else:
        print("Błąd:", response.status_code)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_publication_by_surname('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
