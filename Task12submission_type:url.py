from bs4 import BeautifulSoup
import json
import requests

with open("Top_Rated_Movies.json","r") as f:
    movies=json.load(f)
def scrape_movie_cast(movies):
    i=0
    list_for_actress=[]
    while i<len(movies):
        url=movies[i]['url']
        url_for_cast=requests.get(url)
        soup = BeautifulSoup(url_for_cast.text,"html.parser")
        soup = BeautifulSoup(url_for_cast.text,"html.parser")
        main_actress=soup.find("div",class_="article").get_text()
        main_division=soup.find("div",{"id":"titleCast"})
        table_actress=soup.find("table",class_="cast_list")
        for_tr=soup.find_all("tr")
        k=0
        while k<len(for_tr):
            for_td=for_tr[k].find_all("td")
            j=0
            while j<len(for_td):
                dic={}
                if j==1:
                    for_td_actress=for_td[j].get_text()
                    split_newLines=for_td_actress.splitlines()
                    for_split=split_newLines[1]
                    dic['name']=for_split
                    for_id=for_td[j].a['href']
                    slices=for_id[6:15]
                    dic['imdb_id']=slices
                    list_for_actress.append(dic)
                    break
                j=j+1
            k=k+1
        
        print(i)      
        i=i+1
    with open("scrap_movies_cast.json","w")as f:
        json.dump(list_for_actress,f,indent=4)
scrape_movie_cast(movies)

