from bs4 import BeautifulSoup
import json

with open("full_details_ofMovies.json","r") as f:
    movies_list=json.load(f)

def analyse_actors(movies_list):
    outer_dict={}
    for i in movies_list:
        for_cast=i['cast']
        for j in for_cast:
            for_id=j['imdb_id']
            outer_dict[for_id]={"name":j['name'],"num_of_movie":0}
            for k in movies_list:
                imdbs_list=[x['imdb_id'] for x in k['cast']]
                if for_id in imdbs_list:
                    outer_dict[for_id]['num_of_movie']+=1
    print(outer_dict)
analyse_actors(movies_list)
