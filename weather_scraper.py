from bs4 import BeautifulSoup
import requests

area = input("Enter the Location: ")
url = f"https://www.google.com/search?q=weather+{area}"
headers = ({'User-Agent' : '', 'Accept-Language' : 'en-US,en;q=0.9'})

webpage = requests.get(url, headers=headers)
soup = BeautifulSoup(webpage.content, 'html.parser')
temperature = soup.find(id = "wob_tm").text.strip()
format = soup.find('span', {'aria-label': '°Celsius'}).text.strip()
print(temperature, format, area)
