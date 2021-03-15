
import json
with open("full_details_ofMovies.json","r+") as f:
	movies_list=json.load(f)
# print(movies_list)
exact_dict={}
list_of_result=[]

def analyse_co_actors(movies_list):
	for i in movies_list:
		inner_dicts={}
		actors_list=i['cast'][0:4]
		for j in actors_list:
			inner_dicts[j['imdb_id']]={"name":j['name'],"frequent_co_actors":[]}
			for k in movies_list:
				check_list=k["cast"][0:4]
				imdbs_list=[x['imdb_id'] for x in check_list]
				# for appending whole check list imdb_id
				if j['imdb_id'] in imdbs_list:
					for z in check_list:
						z["num_of_movies"]=0
						for q in movies_list:
							all_cast=q["cast"][0:4]
							imdb_ids=[b['imdb_id'] for b in all_cast]
							if j['imdb_id'] in imdb_ids and z['imdb_id'] in imdb_ids:
								z['num_of_movies']+=1
						if z not in inner_dicts[j['imdb_id']]["frequent_co_actors"]:
							inner_dicts[j['imdb_id']]["frequent_co_actors"].append(z)
						
					# inner_dicts[j['imdb_id']]
		list_of_result.append(inner_dicts)
	
	with open("analyse_co_actors.json","w")as f:
		json.dump(list_of_result,f,indent=4)

analyse_co_actors(movies_list)


		