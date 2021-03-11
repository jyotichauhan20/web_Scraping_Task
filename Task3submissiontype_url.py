import json

with open("Top_Rated_Movies.json","r") as f:
    movies=json.load(f)
    # print(movies)
def decade_by_year(movies):
    decades_dic={"1960":[],"1970":[],"1980":[],"1990":[],"2000":[],"2010":[],"2020":[]}
    for i in movies:
        if i['year']>=1960 and i['year']<=1969:
            decades_dic['1960'].append(i)
        elif i['year']>=1970 and i['year']<=1979:
            decades_dic['1970'].append(i)
        elif i['year']>=1980 and i['year']<=1989:
            decades_dic['1980'].append(i)
        elif i['year']>=1990 and i['year']<=1999:
            decades_dic['1990'].append(i)
        elif i['year']>=2000 and i['year']<=2009:
            decades_dic['2000'].append(i)
        elif i['year']>=2010 and i['year']<=2019:
            decades_dic['2010'].append(i)
        elif i['year']>=2020 and i['year']<=2029:
            decades_dic['2020'].append(i)
    with open("decade_by_year.json","w") as f:
        json.dump(decades_dic,f,indent=4)
decade_by_year(movies)


    

        
