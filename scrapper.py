from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from tqdm import tqdm
import urllib
import os

def get_pictures_subsite(link):
    with urllib.request.urlopen(link) as html:
        bs = BeautifulSoup(html.encode("utf-8"), 'html.parser')
        images = bs.find_all('a')
        for image in images: 
            if "pictures" in str(image) and "cdn" not in str(image):
                return str(image).split('''"''')[1]

def get_subpictures(link):
    image_links = []
    if link is None:
        return []
    with urllib.request.urlopen(link) as html:
        bs = BeautifulSoup(html.encode("utf-8"), 'html.parser')
        images = bs.find_all('img', {'src':re.compile('.jpg')})
        for image in images: 
            if "alt" in str(image):
                image_links.append(str(image).split('''"''')[3])
        return list(set(image_links))

def image_downloader(catalog, target, quota):
    print("downloading {} images...".format(len(quota)), end='\n')
    os.system("mkdir {}".format(catalog))
    for it in tqdm(range(len(quota))):
        urllib.request.urlretrieve(quota[it], "{}/{}.jpg".format(catalog, target))
        target = target + 1
    return target

def pobieracz():
    target = 130
    for i in range(1000):
        print("downloading part {}\n".format(i))
        target = image_downloader(i, target, get_subpictures(get_pictures_subsite("https://myanimelist.net/character/{}/".format(i+target))))
pobieracz()