from bs4 import BeautifulSoup
import json


with open("Movies_Information.json","r") as f:
    movies=json.load(f)
def analyse_movies_language(movies):
    i=0
    count_for_English_movie=0
    count_for_Hindi_movie=0
    count_for_Spanish_movie=0 

    dic_languages={"English":0,"Hindi":0,"Spanish":0}
    while i<len(movies):
        movies_language_list=movies[i]['language']
        j=0
        while j<len(movies_language_list):
            if (movies_language_list[j])=="English":
                count_for_English_movie=count_for_English_movie+1
            elif (movies_language_list[j])=="Hindi":
                count_for_Hindi_movie=count_for_Hindi_movie+1
            elif  (movies_language_list[j])=="Spanish":
                count_for_Spanish_movie=count_for_Spanish_movie+1
            j=j+1
        i=i+1
    dic_languages['English']=count_for_English_movie
    dic_languages['Hindi']=count_for_Hindi_movie
    dic_languages['Spanish']=count_for_Spanish_movie
    print(dic_languages)
analyse_movies_language(movies)










    
    

