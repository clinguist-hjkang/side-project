from selenium import webdriver
import datetime
import re
import pandas as pd

chrome_driver_path = "/Users/admin/development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

pattern = re.compile(r'\s+')

title_lst, content_txt_lst, ratings_lst, writen_date_lst, experienced_date_lst = ([] for i in range(5))

URL = "https://www.tripadvisor.co.kr/Attraction_Review-g294197-d2194168-Reviews-Seoul_Metro-Seoul.html"
driver.get(URL)
tourist_spot = driver.find_element_by_xpath('//*[@id="HEADING"]').text
LAST_PAGE = driver.find_element_by_xpath('//*[@id="component_18"]/div[3]/div/div[8]/div/div/a[6]').text
today_date = pd.to_datetime('today').strftime('%y%m%d')

for i in range(int(LAST_PAGE)-1, int(LAST_PAGE)):
    PAGE = i * 5

    URL = "https://www.tripadvisor.co.kr/Attraction_Review-g294197-d2194168-Reviews-or" + str(
        PAGE) + "-Seoul_Metro-Seoul.html#REVIEWS"

    driver.get(URL)

    titles = driver.find_elements_by_css_selector(".glasR4aX a")
    for title in titles:
        title_txt = title.text
        title_lst.append(title_txt)

    contents = driver.find_elements_by_css_selector('.IRsGHoPm')
    for content in contents:
        content_txt = content.text
        content_txt_lst.append(content_txt)

    bubbles = driver.find_elements_by_css_selector('.nf9vGX55 span')
    for bubble in bubbles:
        ratings = float(bubble.get_attribute('class').split(" ")[1].split("_")[1]) / 10
        ratings_lst.append(ratings)

    when_writen = driver.find_elements_by_css_selector('._2fxQ4TOx span')
    for when in when_writen:
        date = when.text.split()[-2:]
        year = date[0].replace("년","")
        month = date[1].replace("월", "")
        writen_date = month + "-" + year
        writen_date_lst.append(writen_date)

    when_experienced = driver.find_elements_by_css_selector('._34Xs-BQm')
    for when in when_experienced:
        date = when.text.split()[-2:]
        year = date[0].replace("년","")
        month = date[1].replace("월", "")
        experienced_date = month + "-" + year
        experienced_date_lst.append(experienced_date)

df = pd.DataFrame(list(zip(title_lst, content_txt_lst, ratings_lst, writen_date_lst, experienced_date_lst)), columns =['title', 'content', 'ratings', 'writen_date', 'experienced_date'])
filename = today_date + "_" + tourist_spot+"-KR.csv"
filename = filename.lower().replace(" ", "-")
df.to_csv(filename, index=False)

driver.close()
driver.quit()
