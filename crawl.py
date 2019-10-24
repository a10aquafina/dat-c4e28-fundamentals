from urllib.request import urlopen
from bs4 import BeautifulSoup

from collections import*

url = "http://coryn.club/item.php"
connection = urlopen(url)
rawdata= connection.read()
html_comtent= rawdata.decode("utf-8")
soup = BeautifulSoup(html_comtent,"html.parser")
table = soup.find("table","table table-striped")
print(table.pretify())

data=[]
tr_list = table.find_all("tr")
for i in tr_list:
    td = tr_list[i]
    h4=i.h4
    b=h4.b
    name = b.string
    
