from pygal.maps.world import COUNTRIES


def get_country_code(country_name):
    """ Return the pygal 2-digit country code for the given country. """

    for code, name in COUNTRIES.items():
        if name == country_name:
            return code

    # If no country is found, return none
    return None
