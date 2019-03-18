from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import*
from youtube_dl import YoutubeDL

url="https://www.apple.com/itunes/charts/songs/"
conn=urlopen(url)
raw_data=conn.read()
html_content=raw_data.decode("utf-8")
soup=BeautifulSoup(html_content,"html.parser")
section=soup.find("section","section chart-grid")
ul=section.div.ul
li_list=ul.find_all("li")
for i in li_list:
    name=i.h3.string
    link=i.h4.string
    options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 1, # Tell downloader to download only the first entry (audio)
    'format': 'bestaudio/audio'
}
dl=YoutubeDL(options)
dl.download([name+link])