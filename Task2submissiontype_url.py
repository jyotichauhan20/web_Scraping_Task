import json

with open("Top_Rated_Movies.json","r") as f:
    movies=json.load(f)
def group_by_year(movies):
    k=0
    unique_years=[]
    unique_movies_by_year={}
    while k<len(movies):
        if movies[k]['year'] not in unique_years:
            unique_years.append(movies[k]['year'])
        k=k+1
    m=0
    while m<len(unique_years):
        unique_movies_by_year[unique_years[m]]=[]
        c=0
        while c<len(movies):
            if movies[c]['year']==unique_years[m]:
                unique_movies_by_year[unique_years[m]].append(movies[c])
            c=c+1
        m=m+1
    with open("group_by_year.json","w") as f:
        json.dump(unique_movies_by_year,f,indent=4)
group_by_year(movies)
    

