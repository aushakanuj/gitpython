import json

import requests


def get_movies_from_tastedive(a):
    baseUrl = "https://tastedive.com/api/similar"
    key = "364383-movies-XCYHUSC3"
    mov = a
    param = {}
    param["q"] = mov
    param["k"] = key
    param["limit"] = 5
    param["type"] = "movies"
    resp = requests.get(baseUrl, params=param)
    r = resp.json()
    print(json.dumps(r, indent=2))
    return r


def extract_movie_titles(a):
    mov = [i["Name"] for i in a["Similar"]["Results"]]
    return mov


def get_related_titles(list_movies):
    listOfRealtedMovies = []
    for i in list_movies:
        fiveMovies = get_movies_from_tastedive(i)
        listOfFiveMovies = extract_movie_titles(fiveMovies)
        for i in listOfFiveMovies:
            if i not in listOfRealtedMovies:
                listOfRealtedMovies.append(i)
    return listOfRealtedMovies


def get_movie_rating(movs):
    baseUrl = "http://www.omdbapi.com/?apikey=35c7267d&"
    rat = []
    ratings = {}
    for i in movs:
        para = {}
        para["t"] = i
        para["r"] = "json"
        resp = requests.get(baseUrl, params=para)
        p = resp.json()
        rat.append(p)

    for i in rat:
        if i["Response"] == "True":
            if "imdbRating" in i.keys():
                ratings[i["Title"]] = i["imdbRating"]
            else:
                ratings[i["Title"]] = "0.0"
    return ratings


def getSortedMovies(a):
    sorttedList = sorted(a.keys(), key=lambda x: a[x], reverse=True)
    temp = []
    for i in sorttedList:
        if a[i] == "100%":
            temp.append(i)
            sorttedList.remove(i)

    temp.sort()
    sorttedList = temp + sorttedList
    for i in sorttedList:
        print(i, " : ", a[i])


a = 1
while a != 0:
    movieName = input("Enter the movie name for recommendation:\n")
    li = get_movies_from_tastedive(movieName)
    titles = extract_movie_titles(li)

    combinedlist = get_related_titles(titles)
    movieRatings = get_movie_rating(combinedlist)
    getSortedMovies(movieRatings)
    a = int(
        input(
            "Enter (0) to exit the program or press (1) to ask another recommendation\n"
        )
    )
