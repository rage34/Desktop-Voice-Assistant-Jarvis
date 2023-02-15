
import os 
from GoogleImageScrapper.GoogleImageScrapper import GoogleImageScraper

def GoogleImage():
    oo = open('C:\\project\\complete jarvis series\\data.txt','rt')
    query = str(oo.read())
    oo.close()
    pppp = open('C:\\project\\complete jarvis series\\data.txt','r+')
    pppp.truncate(0)
    pppp.close()

    webdriver = "C:\\project\\complete jarvis series\\DataBase\\webdriver\\chromedriver.exe"
    photos = "C:\\project\\complete jarvis series\\DataBase\\googlePhotos\\"
    search_keys = [f"{query}"]
    number = 10
    head = False
    max = (1000,1000)
    min = (0,0)

    for search_key in search_keys:
        image_search = GoogleImageScraper(webdriver,photos,search_keys,number,head,min,max)
        image_url = image_search.find_image_urls()
        image_search.save_images(image_url)
        
    os.startfile("C:\\project\complete jarvis series\\DataBase\\googlePhotos\\")

GoogleImage()