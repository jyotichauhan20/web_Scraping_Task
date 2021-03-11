from bs4 import BeautifulSoup
import requests
import json
import time
import random

with open("Top_Rated_Movies.json","r") as f:
    movies=json.load(f)
def Time_Sleep(movies):
    i=0
    list_foractress=[]
    while i<len(movies):
        movies_url=movies[i]['url']
        Foreachmovies_url=requests.get(movies_url)
        time.sleep(random.randint(1,3))
        soup = BeautifulSoup(Foreachmovies_url.text,"html.parser")
        main_actress=soup.find("div",class_="article").get_text()
        main_division=soup.find("div",{"id":"titleCast"})
        table_actress=soup.find("table",class_="cast_list")
        for_tr=soup.find_all("tr")
        k=0
        dict_foractress={"cast":[]}
        while k<len(for_tr):
            for_tds=for_tr[k].find_all("td")
            l=0
            while l<len(for_tds):
                if l==1:
                    movies_actress=for_tds[l].get_text()
                    split_newLines=movies_actress.splitlines()
                    print(split_newLines)
                    dict_foractress['cast'].append(split_newLines[1])
                    break
                l+=1
            k=k+1
        list_foractress.append(dict_foractress)

        i=i+1
    with open("All_Movies_Cast.json","w") as f:
        json.dump(list_foractress,f,indent=4)

Time_Sleep(movies)
    


