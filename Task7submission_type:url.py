from bs4 import BeautifulSoup
import json

with open("Movies_Information.json","r") as f:
    movies=json.load(f)
def analyse_movies_directors(movies_director):
    i=0
    dic={}
    while i<len(movies):
        director_list=movies[i]['director']
        j=0
        while j<len(director_list):
            dic[director_list[j]]=0
            k=0
            while k<len(movies):
                if director_list[j] in movies[k]['director']:
                    dic[director_list[j]]=dic[director_list[j]]+1
                k=k+1
            j=j+1
        i=i+1
    print(dic)
analyse_movies_directors(movies)








    
    


