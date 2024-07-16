# Weather Scraper

This project fetches the current temperature of a specified location using web scraping techniques with BeautifulSoup and requests libraries in Python.

## Features

- Retrieves the current temperature for a given location.
- Uses web scraping to extract weather data from Google search results.

## Prerequisites

- Python 3.x
- `requests` library
- `beautifulsoup4` library

You can install the required libraries using pip:

```bash
pip install requests beautifulsoup4
```

## Usage

1. Clone the repository or download the script file.

2. Run the script:

```bash
python weather_scraper.py
```

3. Enter the desired location when prompted.

The script will output the current temperature and the unit for the specified location.

## Example

```bash
Enter the Location: New York
25 °Celsius New York
```

## Notes

- Ensure your User-Agent string is set to a valid browser user agent to avoid request blocking by Google.
- The accuracy of the scraped data depends on the structure of the Google search results page, which may change over time.
