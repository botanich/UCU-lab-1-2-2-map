import folium


def create_map(location=[1000, 1000]):
    """
    (list(float)) -> folium.Map
    Creates Map object with given location.
    """

    if location == [1000, 1000]:
        mp = folium.Map()
    else:
        mp = folium.Map(location=location)

    return mp


def build_movie_layer(coord0, movie_data):
    """
    ((float, float), list((str, float, (float, float)))) ->
    folium.FeatureGroup
    Builds map layer by given start location and movie data (list of movie
    names).
    """

    fg = folium.FeatureGroup(name='movie_data')
    to_add_next = [movie_data[0][0]]
    for i in range(1, len(movie_data)):
        if movie_data[i][2] == movie_data[i - 1][2]:
            to_add_next.append(movie_data[i][0])
        else:
            movies_to_add = '|'.join(to_add_next)
            fg.add_child(folium.Marker(location=list(movie_data[i - 1][2]),
                popup=movies_to_add+'|', icon=folium.Icon()))
            to_add_next = [movie_data[i][0]]
    movies_to_add = '|'.join(to_add_next)
    fg.add_child(folium.Marker(location=list(movie_data[-1][2]),
        popup=movies_to_add, icon=folium.Icon()))

    return fg


def build_map(mp, layers):
    """
    (folium.Map, list(folium.FeatureGroup)) -> folium.Map
    Creates map on given map object and feature groups.
    """

    for layer in layers:
        mp.add_child(layer)
    return mp


def save_map(mp, map_path):
    """
    (folium.Map, str) -> None
    Saves given map to the file with path *map_path*
    in the root directory.
    """

    mp.save(map_path)
