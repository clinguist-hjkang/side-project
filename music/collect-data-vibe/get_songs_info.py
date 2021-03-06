from selenium import webdriver
import pandas as pd
import time

chrome_driver_path = "/Users/admin/development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

song_singers, lyrics_bys, song_bys, lyrics, album_titles, album_singers, album_dates, music_types = ([] for i in range(8))

get_filename = '210306_박재범-hrefs.csv'
df = pd.read_csv('get_hrefs/'+ get_filename)

song_hrefs = df['song_href'].tolist()
song_titles = df['song_title'].tolist()

for song_href in song_hrefs:
#### A song's page
    #to keep track on which song we're searching for
    print(song_href)
    driver.get(song_href)

    song_singer = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/h2/span[2]').text
    song_singer = song_singer.split("\n")[1]
    print(song_singer)
    song_singers.append(song_singer)

    lyrics_by = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/div/div[1]').text
    lyrics_by = lyrics_by.replace('작사 ','')
    print(lyrics_by)
    lyrics_bys.append(lyrics_by)

    song_by = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/div/div[2]').text
    song_by = song_by.replace('작곡 ','')
    print(song_by)
    song_bys.append(song_by)

    lyric = driver.find_element_by_xpath('//*[@id="content"]/div[3]/p').text
    print(lyric)
    lyrics.append(lyric)

    print("< 앨범정보 >\n")
    go_to_album_page = driver.find_element_by_xpath('//*[@id="content"]/div[4]/div/div[2]/div/a')
    go_to_album_page = go_to_album_page.get_attribute('href')

    driver.get(go_to_album_page)

    album_title = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[1]/div[2]/div[1]/h2/span[1]').text
    print(album_title)
    album_titles.append(album_title)

    album_singer = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[1]/div[2]/div[1]/h2/span[2]/span/span/a/span').text
    print(album_singer)
    album_singers.append(album_singer)

    album_date = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]').text
    album_date = album_date.replace('.','-')
    print(album_date)
    album_dates.append(album_date)

    music_type = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[1]/div[2]/div[1]/div[1]/span[2]').text
    print(music_type)
    music_types.append(music_type)

    print("========== 여기까지! ==========\n")
    time.sleep(60)

column_names = ['song_title', 'singer', 'lyrics_by', 'song_by', 'lyrics', 'album_title', 'album_singer', 'album_date', 'music_type']
df = pd.DataFrame(list(zip(song_titles, song_singers, lyrics_bys, song_bys, lyrics, album_titles, album_singers, album_dates, music_types)), columns =column_names)

today_date = pd.to_datetime('today').strftime('%y%m%d')
SINGER = ' '.join(Path(FILE).stem.split()[:-1])

filename = today_date + "_" + SINGER+"-info.csv"
filename = filename.lower().replace(" ", "-")
df.to_csv(filename, index=False)


driver.close()
driver.quit()