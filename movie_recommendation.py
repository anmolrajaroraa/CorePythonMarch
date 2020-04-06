import random

movies = {
    "comedy": ["hera pheri", "hangover", "dumb and dumber", "baby's day out", "home alone"],
    "action": ["dabangg", "captain america", "mission impossible", "terminator", "john wick"],
    "thriller": ["nun", "the purge", "american psycho", "limitless", "anabelle"],
    "sci-fi": ["interstellar", "martian", "gravity", "alien", "arrival"],
    "romantic": ["notebook", "one day", "notting hill", "titanic", "a star is born"]
}

user = ["dumb and dumber", "anabelle", "interstellar", "titanic", "martian"]

# task 1 - find categories of all the movies I have seen
# task 2 - sort the categories list extracted above
# task 3 - recommend a movie based on the most watched category

categories_of_watched_movies = []

# ['comedy', 'action', 'thriller', 'sci-fi', 'romantic']
# [4, 5, 1, 1, 1]

sorted_list = []

for watched_movie in user:
    for category in movies:
        if watched_movie in movies[category]:
            categories_of_watched_movies.append(category)
            break
print(categories_of_watched_movies)

for category in movies:
    count = categories_of_watched_movies.count(category)
    sorted_list.append(count)
print(sorted_list)

max_count = max(sorted_list)
index = sorted_list.index(max_count)
categories = list(movies.keys())
most_watched_category = categories[index]
print(most_watched_category)

set1 = set(movies[most_watched_category])
set2 = set(user)
movies_to_be_recommended = list(set1 - set2)
print("Recommended movie is", random.choice(movies_to_be_recommended))
# ["comedy", "action", "thriller", "sci-fi", "romantic"]
# [4,4,1,1,1]
