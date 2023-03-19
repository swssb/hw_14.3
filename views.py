from flask import Blueprint, jsonify, request
from utils import search_film_by_title, search_movies_by_release_years, search_movies_by_rating, search_movies_by_genre

main_blueprint = Blueprint("main_blueprint", __name__)


@main_blueprint.route('/movie/<title>')
def show_movie(title):
    film = search_film_by_title(title)
    return jsonify(film)


@main_blueprint.route('/movie/<int:year_from>/to/<int:year_to>/')
def show_movies_between_years(year_from, year_to):
    films = search_movies_by_release_years(year_from, year_to)
    return jsonify(films)


@main_blueprint.route('/rating/<group>')
def show_movies_for_group(group):
    levels = {'children': ['G'],
              'family': ['G', 'PG', 'PG-13'],
              'adult': ['R', 'NC-17']
              }
    if group in levels:
        level = "\',\'".join(levels[group])
        level = f"\'{level}\'"
    else:
        return jsonify([])
    films = search_movies_by_rating(level)
    return jsonify(films)


@main_blueprint.route('/genre/<genre>')
def show_movies_in_genre(genre):
    films = search_movies_by_genre(genre)
    return jsonify(films)
