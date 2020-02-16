import pandas
import os


def year_movie_location(file_path):
    """(str) -> list(str, str, str)

    Reads location.csv file, getting movie names, years when released and
    locations where were made.

    :param file_name: relative path to csv file with movie data
    :return: list which contains tuples of format (year, movie_name, location)
    """

    data = pandas.read_csv(file_path,
                           encoding='ISO-8859-1', error_bad_lines=False)

    data = data.where(data['location'] != 'NO DATA').dropna()
    data = data.where(data['year'] != 'NO DATA').dropna()
    data = data.where(data['movie'] != 'NO DATA').dropna()
    year_movie_location = zip(data['year'], data['movie'], data['location'])
    return list(year_movie_location)


def data_by_year_and_location_set(year_movie_location):
    """(list(tuple(str, str, str))) ->
    dict(str, dict(str, list(str))), list(str)

    Takes list of tuples in which data in format (year, movie, location) is
    stored.
    """

    data_by_year = {}
    locations_set = set()
    for item in year_movie_location:
        year = item[0]
        movie = item[1]
        location = item[2]

        if year not in data_by_year:
            data_by_year[year] = {}
        if location not in data_by_year[year]:
            data_by_year[year][location] = []
        data_by_year[year][location].append(movie)

        locations_set.add(location)
    return data_by_year, locations_set


def generate_locations_file(locations_set, out_path):
    """(set) -> None
    Generates file where all locations are stored by one in line
    :param locations_set: set with the same locations
    """

    locations_list = list(locations_set)
    locations_list.sort()

    out_file = open(out_path, 'w')
    for item in locations_list:
        out_file.write(item + '\n')
    out_file.close()


def main():
    home = os.path.dirname(__file__)
    in_path = os.path.join(home, r'..\lists\locations.csv')
    print(in_path)
    locations_set = data_by_year_and_location_set(
        year_movie_location(in_path))[1]

    out_path = os.path.join(home, r'..\lists\locations_list.txt')
    generate_locations_file(locations_set, out_path)


if __name__ == "__main__":
    main()
