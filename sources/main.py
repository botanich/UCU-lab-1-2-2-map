import os
import time
import locations_parsing
import folium
import geodesic
import geopy
import map_builder


def main():
    year = input("Please enter a year you would like " +
                        "to have a map for: ")
    latitude, longitude = map(float, input("Please enter your " +
        "location (format: \"*latitude*, *longitude*\"): ").split(', '))
    print("Map is generating, please wait...")

    # Main part-----------------------------------------------------------
    start_time = time.time()

    home = os.path.dirname(__file__)
    in_path = os.path.join(home, r'..\lists\locations.csv')
    year_location_movie_dict = \
        locations_parsing.year_location_movie(in_path)

    country = geodesic.get_country((latitude, longitude))
    coord0 = latitude, longitude

    stop_flag = False
    movie_distance_list = []

    for location in year_location_movie_dict[year]:
        if country in location:
            if stop_flag:
                break

            coord1 = geodesic.get_latitude_longtitude(location)

            if time.time() - start_time > 170: # almost three minutes
                stop_flag = True
                break

            for movie in year_location_movie_dict[year][location]:
                if time.time() - start_time > 170:
                    stop_flag = True
                    break
                movie_distance_list = movie, \
                    geodesic.get_distance(coord0, coord1)
    
    movie_distance_list.sort(key=lambda item: item[-1])
    print(movie_distance_list[: 10])
    #map_builder.label_layer(movie_distance_list[: 10])

    #map_builder.build_map()
    # The end of the main part--------------------------------------------

    print("Finished. Please have a look at the map \"" + str(year) +
            "_movies_map.html\"")


if __name__ == "__main__":
    main()
