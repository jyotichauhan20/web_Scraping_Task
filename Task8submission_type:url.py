from bs4 import BeautifulSoup
import json

with open("Top_Rated_Movies.json","r")as f:
    movies=json.load(f)
def scrap_id_details(movies):
    i=0
    url_list=[]
    while i<len(movies):
        url=movies[i]['url']
        particular_id=url[28:37]
    
        with open("Movies_Information.json","r") as f:
            id_information=json.load(f)
        with open(particular_id+".json","w") as f:
            json.dump(id_information[i],f,indent=4)
        i=i+1

scrap_id_details(movies)

