import csv
import requests
from bs4 import BeautifulSoup
import csv

url = 'https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_chart_achievements_and_milestones#All-Time_Hot_100_achievements_(1958%E2%80%932018)'

html_content = requests.get(url).text

soup = BeautifulSoup(html_content, 'lxml')

song_table = soup.find("table", attrs={"class":"wikitable"})
song_table_data = song_table.tbody.find_all("tr")

headings = []
for row in song_table_data:
    headings.append(row)

data = []

for i, row in enumerate(headings):
    rowDict = {}
    if i == 0:
        rowDict['headers'] = [em.text for em in row.find_all("th")]
    else:
        rowDict[i] = [em.text for em in row.find_all("td")]
    data.append(rowDict)

with open('WebScrape.csv', mode='w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(data[0])
