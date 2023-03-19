import sqlite3


def search_film_by_title(title):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        query = (f""" 
                SELECT show_id, title, country, release_year, listed_in, description FROM netflix
                WHERE title = '{title}'
                ORDER BY release_year DESC
                LIMIT 1 
        """)
        cursor.execute(query)
        result = cursor.fetchall()
        json_format = {
            "title": result[0][1],
            "country": result[0][2],
            "release_year": result[0][3],
            "genre": result[0][4],
            "description": result[0][5]
        }
        return json_format


def search_movies_by_release_years(from_year, to_year):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        query = (f""" 
                SELECT title, release_year FROM netflix
                WHERE release_year BETWEEN {from_year} AND {to_year}
                ORDER BY title
                LIMIT 100
        """)
        cursor.execute(query)
        result = cursor.fetchall()
        json_format = []
        for title in result:
            json_format.append({"title": title[0], "release_year": title[1]})
        return json_format


def search_movies_by_rating(level):
    with sqlite3.connect('netflix.db') as connection:
        print(level)
        cursor = connection.cursor()
        query = (f""" 
                SELECT title, rating, description FROM netflix
                WHERE rating IN ({level})
                    
        """)
        cursor.execute(query)
        result = cursor.fetchall()
        json_format = []
        for title in result:
            json_format.append({"title": title[0], "rating": title[1], "description": title[2]})
        return json_format


def search_movies_by_genre(genre):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        query = (f""" 
                SELECT title, description, listed_in, release_year FROM netflix
                WHERE listed_in LIKE '%{genre}%'
                ORDER BY release_year DESC
                LIMIT 10

        """)
        cursor.execute(query)
        result = cursor.fetchall()
        json_format = []
        for title in result:
            json_format.append({"title": title[0], "description": title[1]})
        return json_format


def search_movies_with_actors(actor1, actor2):
    ''' Поиск актеров '''
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        query = (f"""
                SELECT "cast" FROM netflix
                WHERE "cast" LIKE "%{actor1}%" AND "cast" LIKE "%{actor2}%" 

                """)
        cursor.execute(query)
        result = cursor.fetchall()
        actors = []
        for cast in result:
            actors.extend(cast[0].split(', '))
            new_actors = []
        for actor in actors:
            if actor not in (actor1, actor2):
                if actors.count(actor) > 2:
                    new_actors.append(actor)

        return set(new_actors)


def search_movies_by_type_year_genre(type, year, genre):
    ''' Поиск фильма по трем параметрам: тип, год, жанр '''
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        query = (f""" 
                SELECT title, description, type, release_year, listed_in FROM netflix
                WHERE type = '{type}' AND release_year = {year} AND listed_in LIKE '%{genre}%'                
                """)
        cursor.execute(query)
        result = cursor.fetchall()
        json_file = []
        for element in result:
            json_format = {"title": element[0], "description": element[1]}
            json_file.append(json_format)
        return json_file

# films = search_movies_by_release_years(2000, 2017)
# print(films)

# films = search_movies_with_actors('Rose McIver', 'Ben Lamb')
# print(films)
# films = search_movies_by_rating('PG',"")
# print(films)
# films = search_movies_by_genre('Comedy')
# print(films)

# films = search_movies_by_type_year_genre('Movie', 2020, 'Comedy')
# print(films)
