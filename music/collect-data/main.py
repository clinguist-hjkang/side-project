from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/admin/development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

##### Jay PARK's page
# driver.get("https://vibe.naver.com/artist/101695/tracks")
# song = driver.find_element_by_css_selector(".song .title_badge_wrap a")
# print(song.text)

# 각 곡에 대해서 (for ...:)
# 곡 페이지로 들어가서 아래의 정보 불러오고 탭 닫기


##### A song's page
driver.get("https://vibe.naver.com/track/43986956")
song = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/h2/span[1]').text
song = song.split("\n")[1]
print(song)

singer = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/h2/span[2]').text
singer = singer.split("\n")[1]
print(singer)

lyrics_by = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/div/div[1]').text
lyrics_by = lyrics_by.replace('작사 ','')
print(lyrics_by)

song_by = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/div/div[2]').text
song_by = song_by.replace('작곡 ','')
print(song_by)

lyrics = driver.find_element_by_xpath('//*[@id="content"]/div[3]/p').text
print(lyrics)




driver.close()
driver.quit()
