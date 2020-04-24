from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
#import urllib.request
from pytube import YouTube
driver=webdriver.Firefox(executable_path='/home/proma/youtube_playlist_downloader/source/geckodriver')

driver.get("https://www.youtube.com/")
#### get suggested videos ####
filter = input("Enter category of search...be specific to get better results...\n")

Xpath = '//input[@name="search_query"]'
#search_query.clear()
driver.find_element_by_xpath(Xpath).clear()
driver.find_element_by_xpath(Xpath).send_keys(filter)
driver.find_element_by_id("search-icon-legacy").click()

###   download  ###
user_data = driver.find_elements_by_xpath('//*[@id="video-title"]')
links = {}
c = 0;
for i in user_data:
            if c > 1:
                links[(i.get_attribute('title'))] = i.get_attribute('href')
            c=c+1
            if c > 5:
                break


for link in links:
    print(link, end =" ")
    print(links[link])

video = input("enter the number of video to be downloaded\n")

c = 0
for l in links:
    c=c+1
    if c == video:
        link = links[l]
        break
#lin = list(links)[video-1]
#link = links[lin]
yt = YouTube(link)

    # Downloaded video will be the best quality video
stream = yt.streams.filter(progressive=True,
                file_extension='mp4').order_by(
                'resolution').desc().first()
try:
        stream.download("/home/proma/Downloads")
        # printing the links downloaded
        print("Downloaded: ", link)
except:
        print('Some error in downloading: ', link)
