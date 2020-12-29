import numpy as np

def direction(lat1, lon1, lat2, lon2):
    lat1 = np.radians(lat1)
    lat2 = np.radians(lat2)
    lon1 = np.radians(lon1)
    lon2 = np.radians(lon2)
    delta_lon = lon2 - lon1
    a = np.cos(lat2)*np.sin(delta_lon)
    b = np.cos(lat1)*np.sin(lat2)-np.sin(lat1)*np.cos(lat2)*np.cos(delta_lon)
    direction = np.arctan2(a, b)
    # cyclical transform
    direction_sin = np.sin(direction)
    direction_cos = np.cos(direction)
    return (direction_sin, direction_cos)
