import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


def extract_population_number(tekst):
    tekst = tekst.strip()
    match = re.search(r"\d[\d\s]*\d", tekst)
    if match:
        return match.group().strip()
    return None


def get_population_from_infobox(city_name):
    city_name_url = city_name.strip().replace(" ", "_")
    url = f'https://pl.wikipedia.org/wiki/{city_name_url}'
    print(f"Sprawdzany URL: {url}")

    try:
        response = requests.get(url, timeout=6)
        response.raise_for_status()
    except:
        return None

    soup = BeautifulSoup(response.content, 'html.parser')
    infobox = soup.find("table", class_="infobox")
    if not infobox:
        return None

    rows = infobox.find_all("tr")
    for row in rows:
        header = row.find("th")
        if not header:
            continue


        header_text = header.get_text().replace('\xa0', ' ').lower()
        if any(klucz in header_text for klucz in ["populacja", "liczba ludności"]):
            value_cell = row.find("td")
            if value_cell:
                tekst = value_cell.get_text()
            else:
                tekst = header_text
            liczba_ludnosci = extract_population_number(tekst)
            if liczba_ludnosci:
                return liczba_ludnosci

    return None

input_file = "C:/Users/a.koczakowska/Desktop/Wielkosc_miejscowosci/Próba TUR.xlsx"
df = pd.read_excel(input_file)

if 'Miejscowość' not in df.columns:
    print("Brak kolumny 'Miejscowość' w pliku excel")
else:
    print("jest w pliku")

df = df.assign(liczba_ludności = [None] * len(df))

for index, row in df.iterrows():
    miasto = str(row['Miejscowość']).strip()
    populacja = get_population_from_infobox(miasto)


    if populacja is None:
        woj = str(row['Województwo głównej siedziby']).strip().lower()
        if woj:
            miasto_rozszerzone = f"{miasto}_(województwo_{woj})"
            populacja = get_population_from_infobox(miasto_rozszerzone)
            print(f"🔁 Próba ponowna z: {miasto_rozszerzone}")

    df.at[index, 'liczba_ludności'] = populacja
    print(f"{index + 1}/{len(df)} - {miasto}: {populacja}")


df.to_excel(input_file, index=False)
print("Dane zapisane do pliku.")



