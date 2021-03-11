from bs4 import BeautifulSoup
import json
import requests

with open("Top_Rated_Movies.json","r") as f:
    movies=json.load(f)
def scrap_movies_details(movies):
    c=0
    information_list=[]
    while c<len(movies):
        information_dict ={}
        url=(movies[c]['url'])
        movie_name=movies[c]['name']
        information_dict['name']=movie_name
        Foreachmovies_url=requests.get(url)
        soup = BeautifulSoup(Foreachmovies_url.text,"html.parser")
        main_division=soup.find("div",{"id":"titleDetails"})
        txt_block_division=main_division.find_all("div",class_="txt-block")
        main_actress=soup.find("div",class_="article").get_text()

        table_actress=soup.find("table",class_="cast_list")
        for_tr=table_actress.find_all("tr")
        k=0
        while k<len(txt_block_division):
            if k==1:
                movie_country=txt_block_division[k].get_text()
                split_movies=movie_country.splitlines()
                i=0
                split_movies.pop(0)
                split_movies.pop(0)
                while i<len(split_movies):
                    if split_movies[i]=="|":
                        split_movies.remove("|")
                    i=i+1
                information_dict['country']=split_movies
            elif k==2:      
                movie_language=txt_block_division[k].get_text()
                split_language=movie_language.splitlines()
                j=0
                split_language.pop(0)
                split_language.pop(0)
                while j<len(split_language):
                    if split_language[j]=="|":
                        split_language.remove("|")
                    j=j+1
                information_dict['language']=split_language
            elif k==12:
                run_time=txt_block_division[k].get_text()
                split_runtime=run_time.splitlines()
                split_runtime.pop(0)
            
                split_runtime.pop(0)
                without_list=split_runtime[0]
                information_dict['runtime']=without_list
            k=k+1
        m=0
        list_for_actress=[]
        while m<len(for_tr):
            for_td=for_tr[m].find_all("td")
            z=0
            while z<len(for_td):
                dic={}
                if z==1:
                    for_td_actress=for_td[z].get_text()
                    split_newLines=for_td_actress.splitlines()
                    for_split=split_newLines[1]
                    dic['name']=for_split
                    for_id=for_td[z].a['href']
                    slices=for_id[6:15]
                    dic['imdb_id']=slices
                    list_for_actress.append(dic)
                    break
                z=z+1
            m=m+1
        information_dict['cast']=list_for_actress
        For_genre=soup.find("div",class_="subtext").a.get_text()
        for_list=[]
        for_list.append(For_genre)
        information_dict['genre']=for_list
        For_poster=soup.find("div",class_="poster").a.img['src']
        split_poster=For_poster.splitlines()
        without_list=split_poster[0]
        information_dict['poster']=without_list
        For_bio=soup.find("div",class_="summary_text").get_text()
        split_bio=For_bio.splitlines()
        without_list_bio=split_bio[1]
        remove_spaces=without_list_bio.lstrip()
        information_dict['bio']=remove_spaces
        For_director=soup.find("div",class_="credit_summary_item").a.get_text()
        list_for_director=[]
        list_for_director.append(For_director)
        information_dict['director']=list_for_director
        information_list.append(information_dict)
        # print(c)
        c=c+1      
    with open("full_details_ofMovies.json","w") as f:
        json.dump(information_list,f,indent=4)
    
scrap_movies_details(movies)

