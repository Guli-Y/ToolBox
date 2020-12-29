import numpy as np
import googlemaps


def haversine_distance(lat1, lon1, lat2, lon2):
    lat1 = np.radians(lat1)
    lat2 = np.radians(lat2)
    lon1 = np.radians(lon1)
    lon2 = np.radians(lon2)
    delta_lon = lon2 - lon1
    delta_lat = lat2 - lat1
    a = (np.sin(delta_lat / 2.0)) ** 2 + np.cos(lat1) * np.cos(lat2) * (np.sin(delta_lon / 2.0)) ** 2
    haversine_distance = 6371000 * 2 * np.arcsin(np.sqrt(a))
    return haversine_distance

def manhattan_distance(lat1, lon1, lat2, lon2):
    return abs(lat2 - lat1) + abs(lon2 - lon1)

############ googlemap_distance #######################
API_key = ''

def googlemap_distance(lat1, lon1, lat2, lon2):
    gmaps = googlemaps.Client(key=API_key)
    try:
        result = gmaps.distance_matrix((lat2, lon2), (lat1, lon1) mode='driving')
        distance = result["rows"][0]["elements"][0]["distance"]["value"]
    except:
        print('not found on google map')
        distance = np.nan
    return distance
