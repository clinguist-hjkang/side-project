from bs4 import BeautifulSoup
import pandas as pd
import datetime
from pathlib import Path

FILE = 'html/박재범 VIBE(바이브).html'

with open(FILE) as html_file:
    html_data = html_file.read()

song_hrefs, song_titles = ([] for i in range(2))
soup = BeautifulSoup(html_data, 'lxml')

table_body = soup.find('tbody')
rows = table_body.find_all('tr')

for row in rows:
    cols = row.find_all('td')
    for col in cols:
        a_tag = col.find(name='a', class_='link_text')
        if a_tag:
            href = a_tag.get("href")
            song_hrefs.append(href)
            title = a_tag.get("title")
            song_titles.append(title)


column_names = ['song_title', 'song_href']
df = pd.DataFrame(list(zip(song_titles, song_hrefs)), columns=column_names)

today_date = pd.to_datetime('today').strftime('%y%m%d')
SINGER = ' '.join(Path(FILE).stem.split()[:-1])

filename = today_date + "_" + SINGER+".csv"
filename = filename.lower().replace(" ", "-")

df.to_csv(filename, index=False)

