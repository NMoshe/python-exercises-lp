from selenium import webdriver  # for webdriver
import os
import requests

# Create folder if the folder 'imgur' currently does not exist.
os.makedirs('imgur', exist_ok=True)
print('Enter Name of Images to download: ')
images = input().split()

option = webdriver.ChromeOptions()
option.add_argument('--headless')
browser = webdriver.Chrome(options=option)

browser.get('http://imgur.com/search?q=' + '+'.join(images))

matches = [elem.find_element_by_tag_name('img').get_attribute('src')
           for elem in browser.find_elements_by_class_name('image-list-link')]


def getFullImage(arr):
    imagesD = []
    for i in arr:
        i = i.replace('b.', '.')
        imagesD.append(i)
    return imagesD


for link in getFullImage(matches):
    print('Downloading images %s...' % link)
    res = requests.get(link)
    res.raise_for_status()

    imageFile = os.path.join('imgur', os.path.basename(link))
    with open(imageFile, 'wb') as f:
        for chunk in res:
            f.write(chunk)

print(f'Downloaded {len(matches)} pictures of ' + ' '.join(images) + ' from Imgur.')

