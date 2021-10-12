import requests
from bs4 import BeautifulSoup

imdburl = "https://www.imdb.com/chart/top/"
header={"accept-language":"tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7"}
r=requests.get(imdburl,headers=header)

soup = BeautifulSoup(r.content,"html.parser")

get_data=soup.find_all("table",{"class":"chart full-width"})
film_table = (get_data[0].contents)[len(get_data[0].contents)-2]
film_table = film_table.find_all("tr")
f = open("C:/Users/hupes/Desktop/IMDBTOP250","w")

for film in film_table:
    filmbasliklar = film.find_all("td",{"class":"titleColumn"})
    film_name=film.find_all("a")[1].text
    # film_name=filmbasliklar[0].tex
    # film_name=film_name.replace("\n","")
    print(film_name)
    f.write(film_name+"\n")
    print("*******************************")