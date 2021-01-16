from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

sess = requests.session()

html = urlopen("https://ide.goorm.io/my/container/myServer")
bsObject = BeautifulSoup(html, "html.parser")

github = bsObject.find_all('a')
print(github[5].get('title'))
