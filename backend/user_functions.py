# utility functions for users to use
from imdb import IMDb, IMDbError
from apiRequests import *
import random

"""
This one uses RAPID API IMDb. Basic recommendation 
"""
# give you a list of similar movies
def search_for_similar():
    show_name = input("Name of show: ")
    show_id = search(show_name)
    recommended_ids = get_moreLikeThis(show_id, "US", "US")
    titles = []
    for i in recommended_ids:
        # get metadata of the given id
        title = get_metadata(i, "US")
        # get the title and put it into a list with pair id
        name = title[i]["title"]["title"]
        titles.append((name,i))
    return titles

def detailed_info(title, id):
    data = get_metadata(id, "US")
    print("Title: ", title)
    # print(id)
    print("Type: ", data[id]["title"]["titleType"])
    print("Running time (minutes): ", data[id]["title"]["runningTimeInMinutes"])
    print("Year: ", data[id]["title"]["year"])
    print("Rated: ", data[id]["certificate"])
    print("Rating: ", data[id]["ratings"]["rating"])
    print("Genres: ", end='')
    s = ""
    summary = " "
    for i in data[id]["genres"]:
        s+= i + " "
        # print(i, end=' ')
    print("\nImage URL: ", data[id]["title"]["image"]["url"])
    result = [title, data[id]["title"]["year"], s, data[id]["title"]["image"]["url"], data[id]["certificate"], data[id]["title"]["runningTimeInMinutes"], summary, data[id]["title"]["titleType"], id] 
    return result

"""
These uses IMDbPy library
"""
# get title, movie ids base on title
def get_movie_id(title):
    ids = []
    ia = IMDb()
    movies = ia.search_movie(title)
    for m in movies:
        id = m.getID()
        ids.append((m, id))
    return ids

# warning: some id do not have a rating so it will have to be skipped with try except:
def get_movie_rating(id):
    ia = IMDb()
    movie = ia.get_movie(id)
    return movie['rating']

# lst = get_movie_id('Matrix')
# for i, j in lst:
#     try:
#         rating = get_movie_rating(j)
#         print(i, rating)
#     except:
#         pass

def get_movie_info(id):
    ia = IMDb()
    m = ia.get_movie(id)
    # use print(m.keys()) to see more options avaiable.
    print(m['title'])
    print(m['year'])
    print(m['rating'])
    directors = m['directors']
    direcStr = ' '.join(map(str, directors))
    print(f'directors: {direcStr}')
    for genre in m['genres']:
        print(genre)

# return movie ids searched by keyword
def filter_by_keyword(keyword):
    ia = IMDb()
    movies = ia.get_keyword(keyword)
    ids = []
    for m in movies:
        ids.append(m.getID())
    return ids

def filter_by_genre(id, genre):
    pass

# get_movie_info(1234567)
# data base connection example

# exec(open("backend/database.py").read())
# connection = open_DBConnection()
# # print(connection)
# # name, type, ID
# print(res[8])
# set_data(connection, res[0], "movie", res[8])
# list_of_items = get_by_id(connection, "tt4154756", table="media")
# for i in list_of_items:
#     print(i)
# delete_data(connection, "tt4154756", table="media")
# list_of_items = get_by_id(connection, "tt4154756", table="media")
# if list_of_items is not None:
#     for i in list_of_items:
#         print(i)
# else:
#     print("empty")
# close_DBConnection(connection)




# getting top 250 movies and bottom 100 movies
# https://www.youtube.com/watch?v=vzOdCPV7zvs

# moves goes from 1 to seven digit number 
# for i in range(1,99):
#     randNum = random.randint(1,99999)
#     ia = IMDb()
#     movie = ia.get_movie(randNum)
#     try:
#         if "Episode" in movie["title"]:
#             continue
#         print(i, movie["title"])
#     except::
#         print(e)
#         pass
# movie = ia.get_movie('9999999')
# print(movie["title"])
# top = ia.get_top250_movies()
# for movie in top:
#     id = movie.getID()
#     m = ia.get_movie(id)
#     print(id)
#     print(m.keys())
#     print(m['title'])
#     print(m['year'])
#     print(m['rating'])
#     directors = m['directors']
#     direcStr = ' '.join(map(str, directors))
#     print(f'directors: {direcStr}')
#     for genre in m['genres']:
#         print(genre)

# bottom = ia.get_bottom100_movies()


