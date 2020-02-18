import pandas
import os
import random
import geopy


def year_location_movie(file_path):
    """(str) -> dict(str, dict(str, list(str)))

    Reads location.csv file, getting movie names, years when released and
    locations where were made.

    :param file_name: relative path to csv file with movie data
    :return: dictionary with year as key which contains dictionary with
        location as key which contains list of movies that were made in that
        year in that location
    """

    data = pandas.read_csv(file_path, encoding='ISO-8859-1',
        error_bad_lines=False, warn_bad_lines=False)

    data = data.where(data['location'] != 'NO DATA').dropna()
    data = data.where(data['year'] != 'NO DATA').dropna()
    data = data.where(data['movie'] != 'NO DATA').dropna()
    year_location_movie = zip(data['year'], data['location'], data['movie'])
    year_location_movie_dict = {}
    for item in year_location_movie:
        #print(item[0], item[1], item[2])
        if item[0] not in year_location_movie_dict:
            year_location_movie_dict[item[0]] = {}
        if item[1] not in year_location_movie_dict[item[0]]:
            year_location_movie_dict[item[0]][item[1]] = []
        year_location_movie_dict[item[0]][item[1]].append(item[2])

    return year_location_movie_dict
