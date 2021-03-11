from bs4 import  BeautifulSoup 
import requests  
import json  

     

def scrap_top_movies():
    url = "https://www.imdb.com/chart/top/"
    page = requests.get(url)
    soup = BeautifulSoup(page.text,"html.parser")

    soup.find("h1")
    print(soup.find("h1").get_text())
    main_division=soup.find("div",class_="lister")
    tbody_division=main_division.find("tbody",class_="lister-list")
    table_rows=tbody_division.find_all("tr")
    index=1
    movies_list=[]
    for i in table_rows:
        each_movieDict={}
        movie_name=(i.find("td",class_="titleColumn").a.get_text())
        each_movieDict['name']=movie_name
        movie_year=(i.find("td",class_="titleColumn").span.get_text())
        length=len(movie_year)
        j=0
        output=""
        while j<length:
            if movie_year[j]=="(" or movie_year[j]==")": 
                j=j+1
                continue
            else:
                output+=movie_year[j]
                j=j+1
                    
        each_movieDict['year']=int(output)
        movie_position=index
        index=index+1
        each_movieDict['position']=movie_position
        movie_rating=(i.find("td",class_="ratingColumn imdbRating").strong.get_text())
        each_movieDict['Rating']=(float(movie_rating))
        
        url=i.find("td",class_="titleColumn").a["href"]
        movie_url="https://www.imdb.com/"+url
        each_movieDict['url']=movie_url

        

        # movie_url="https://www.imdb.com/"+i.find("td",class_="titleColumn").a["href"]
        # print(movie_url)
        movies_list.append(each_movieDict)

    
    with open("Top_Rated_Movies.json","w") as f:
        json.dump(movies_list,f,indent=4)
    return(movies_list)
scrap_top_movies()

    


