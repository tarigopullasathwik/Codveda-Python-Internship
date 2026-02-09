import requests
from bs4 import BeautifulSoup
import csv

url = "https://news.ycombinator.com/"
response = requests.get(url)

print("Status Code:", response.status_code)  # Debug

soup = BeautifulSoup(response.text, "html.parser")

# Try a different selector (site may have changed)
titles = soup.find_all("span", class_="titleline")

print("Number of titles found:", len(titles))  # Debug

with open("scraped_data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title"])
    for title in titles:
        link = title.find("a")
        if link:
            writer.writerow([link.text])

print("✅ Data scraped and saved to scraped_data.csv")
