import geopy.distance
import geopy.geocoders


geolocator = geopy.geocoders.Nominatim(user_agent='botanich')


def get_country(coord):
    """
    ((float, float)) -> str
    Returns country by coordinates (latitude and longtitude)
    """

    geolocator = geopy.geocoders.Nominatim(user_agent='dark_red_butterfly',
        timeout=10)
    country = str(geolocator.reverse(coord, language='en')).split(', ')[-1]
    if country == 'United States of America':
        country = 'USA'
    elif country == 'United Kingdom':
        country = 'UK'

    return country


def get_distance(coord1, coord2):
    """
    ((float, float), (float, float)) -> float
    Returns distance between two given as latitude and longtitude points
    (in meters)
    """

    return geopy.distance.great_circle(coord1, coord2).meters


def get_latitude_longtitude(location):
    """
    (str) -> (float, float)
    By given location returns
    """

    return geolocator.geocode(location)
