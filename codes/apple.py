import requests
import json

def get_movies_from_tastedive(a):
    baseUrl="https://tastedive.com/api/similar"
    key="364383-movies-XCYHUSC3"
    mov=a
    param={}
    param["q"]=mov
    param["k"]=key
    param["limit"]=5
    param["type"]="movies"
    resp=requests.get(baseUrl,params=param)
    p=resp.json()
    return p


def extract_movie_titles(a):
    mov=[i["Name"] for i in a["Similar"]["Results"]]
    return mov


def get_related_titles(list_movies):
    listOfRealtedMovies=[]
    for i in list_movies:
        fiveMovies=get_movies_from_tastedive(i)
        listOfFiveMovies=extract_movie_titles(fiveMovies)
        for i in listOfFiveMovies:
            if i not in listOfRealtedMovies:
                listOfRealtedMovies.append(i)
    return listOfRealtedMovies

def get_movie_rating(movs):
    api="e2a46df1"
    baseUrl="http://www.omdbapi.com/?apikey=35c7267d&"
    rat=[]
    ratings={}
    for i in movs:
        para={}
        para["t"]=i
        para["r"]="json"
        resp=requests.get(baseUrl,params=para)
        p=resp.json()
        rat.append(p)
    print(json.dumps(rat,indent=2))
    for i in rat:
        if i["Response"]="True"
            for j in i["Ratings"]:
                if j["Source"]=="Rotten Tomatoes":
                    ratings[i["Title"]]=(i["Ratings"][1]["Value"])
    return ratings
l="superman"
li=get_movies_from_tastedive(l)
titles=extract_movie_titles(li)
combinedlist=get_related_titles(titles)
get_movie_rating(combinedlist)