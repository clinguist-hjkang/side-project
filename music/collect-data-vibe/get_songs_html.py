import pandas as pd
import urllib.request, urllib.parse
import ssl

# get_filename = input("Enter the file name (include the CSV extension): ")
get_filename = '210306_박재범-hrefs.csv'
df = pd.read_csv('get_hrefs/'+ get_filename)

for _, row in df.iterrows():
    song_href = row['song_href']
    song_title = row['song_title'].replace('/','&')

    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(song_href, context=context)
    webContent = response.read()

    today_date = pd.to_datetime('today').strftime('%y%m%d')
    SINGER = get_filename.split('_')[-1].split('-')[0]
    save_filename = today_date + '_' + SINGER+'-' + song_title + '.html'
    filepath = "get_songs_html/" + save_filename

    f = open(filepath, 'wb')
    f.write(webContent)
    f.close


