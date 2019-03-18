from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import*
from youtube_dl import YoutubeDL
url="https://www.apple.com/itunes/charts/songs/"


raw_data=urlopen(url).read()
html_content=raw_data.decode("utf-8")
soup=BeautifulSoup(html_content,"html.parser")
ul=soup.find("ul","section-content")
data=[]
li_list= ul.find_all("li")
for li in range(len(li_list)):
    li=li_list[li]
    h4=li.h4
    a=h4.a
    name=a.string
    link=url +a["href"]
    new={
        "name":name,
        "link":link
    }
    data.append(new)
pyexcel.save_as(records=data,dest_file_name="singer_song.xlsx")

dl=YoutubeDL()
print(link)
# dl.d Download ([link])