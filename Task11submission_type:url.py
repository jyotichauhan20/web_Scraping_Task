from bs4 import BeautifulSoup
import json

with open("Movies_Information.json","r")as f:
    movies_genre=json.load(f)
def Analyse_Movies_Genre(movies_genre):
    i=0
    dic_for_genre={}
    while i<len(movies_genre):
        For_genre=movies_genre[i]['genre']
        k=0
        while k<len(For_genre):
            dic_for_genre[For_genre[k]]=0
            j=0
            while j<len(movies_genre):
                if For_genre[k] in movies_genre[j]['genre']:
                    dic_for_genre[For_genre[k]]+=1
                j=j+1
            k=k+1
        i=i+1
    with open("Analyse_Movies_Genre.json","w") as f:
        json.dump(dic_for_genre,f,indent=4)
Analyse_Movies_Genre(movies_genre)



from bs4 import BeautifulSoup
import json

with open("full_details_ofMovies.json","r")as f:
    movies_list=json.load(f)
    print(movies_list)

# def frequent_co_actors(movies_list):
#     i=0
#     dict_for_all_actors={}
#     while i<len(movies_list):
#         cast=movies_list[i]['cast'][0:4]
#         for j in cast:
#             id_for_key=j["imdb_id"]
#             name_for_actors=j['name']
#             dict_for_all_actors[id_for_key]={'name':name_for_actors,"frequent_co_actors":[]}
#             k=0
#             while k<len(movies_list):
#                 if j in movies_list[k]['cast'][0:4]:
#                     dict_for_all_actors[id_for_key]['frequent_co_actors'].append(movies_list[k]['cast'][0:4])
#                 k=k+1
#         i=i+1
#         print(dict_for_all_actors)
#         break
# frequent_co_actors(movies_list)