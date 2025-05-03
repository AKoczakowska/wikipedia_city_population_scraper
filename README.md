# City Population Data Prep

This Python tool extracts the population size of cities from Wikipedia and appends the data to an Excel file.  
It was created as part of a data analysis process to support a research project requiring city-level population data.

## 📌 Features

- Scrapes population data from the infobox on Wikipedia pages (in Polish).
- Handles missing matches by retrying with city + voivodeship.
- Adds population data as a new column in your Excel file.
- Automatically saves changes back to the file.

## 🔧 Technologies Used

- `Python 3`
- `requests`
- `BeautifulSoup (bs4)`
- `pandas`
- `re` (regular expressions)

## 📂 Input File Structure

The script reads from an Excel file with at least the following columns:

- `Miejscowość` – name of the city or town
- `Województwo głównej siedziby` – voivodeship, used when the city name is ambiguous

Example row:
| Miejscowość | Województwo głównej siedziby |
|-------------|------------------------------|
| Pęgów       | dolnośląskie                 |

## ▶️ How to Use

1. Place your Excel file at the desired path and update the `input_file` variable in the script.
2. Run the script.
3. The script will:
   - Access Wikipedia for each city
   - Extract population if available
   - Retry with extended city name (including voivodeship) if needed
   - Save the updated Excel file (overwrites the original)

## 📁 Example Output

A new column `liczba_ludności` will be added to your Excel file:

| Miejscowość | Województwo głównej siedziby | liczba_ludności |
|-------------|------------------------------|------------------|
| Gdańsk      | pomorskie                    | 486,022          |
| Pęgów       | dolnośląskie                 | 3,123            |

## ⚠️ Notes

- The script is tailored to Wikipedia in **Polish** (`pl.wikipedia.org`).
- Not all small towns or ambiguous names may have available data.
- Some pages may fail to load due to Wikipedia limitations or structure changes.

## 📄 License

MIT License

## 👩‍💻 Author

Created by AKoczakowska
