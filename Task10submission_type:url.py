from bs4 import BeautifulSoup
import json

with open("Movies_Information.json","r") as f:
    movies_information=json.load(f)
def Analyse_Language_and_Directors(movies_information):
    i=0
    dic1={}
    while i<len(movies_information):
        director=movies_information[i]['director']
        k=0
        dic2={}
        while k<len(director):
            Director_for_key=director[k]
            dic1[Director_for_key]={}
            for j in movies_information[i]["language"]:
                dic1[Director_for_key][j]=0
                for s in movies_information:
                    if Director_for_key in s["director"] and j in s["language"]:
                        dic1[Director_for_key][j]+=1
            k=k+1
        i=i+1
    with open("Analyse_Language_and_Directors.json","w") as f:
        json.dump(dic1,f,indent=4)
Analyse_Language_and_Directors(movies)





