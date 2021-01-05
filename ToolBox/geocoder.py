import hereby

HERE_API_KEY = ''

def reverse_geocoder(coords, key=HERE_API_KEY):
    geoapi = herepy.GeocoderReverseApi(key)
    result = geoapi.retrieve_addresses(coords).as_dict()
    address = result["items"][0]["address"]['label']
    return address

def geocoder(address, key=HERE_API_KEY):
    geoapi = herepy.GeocoderApi(api_key=key)
    result = geoapi.free_form(address).as_dict()
    coords = result["items"][0]["position"]
    coords = {k.lower():v for k, v in coords.items()}
    return coords
