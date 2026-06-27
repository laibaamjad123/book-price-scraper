import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com"
response = requests.get(url)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "html.parser")

titles = soup.select("h3 a")
prices = soup.select("p.price_color")

with open("C:/Users/dell/Desktop/books.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price"])
    
    for title, price in zip(titles, prices):
        writer.writerow([title.get("title"), price.text.strip()])

print("Done! Clean CSV file created!")