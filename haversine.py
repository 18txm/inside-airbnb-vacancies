import math

EARTH_RADIUS_KM = 6371


def to_radians(degrees):
    return degrees * math.pi / 180


def get_distance(lat1, lon1, lat2, lon2):
    r_lat1 = to_radians(lat1)
    r_lat2 = to_radians(lat2)
    d_lat = to_radians(lat2 - lat1)
    d_lon = to_radians(lon2 - lon1)
    a = ((math.sin(d_lat / 2) ** 2) +
         (math.cos(r_lat1) * math.cos(r_lat2) * (math.sin(d_lon / 2) ** 2)))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return EARTH_RADIUS_KM * c
