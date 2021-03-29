from pygal.maps.world import COUNTRIES


def get_country_code(country_name):
    """ Return the pygal 2-digit country code for the given country. """

    for code, name in COUNTRIES.items():
        if name == country_name:
            return code

        else:
            if country_name == 'Yemen, Rep.':
                return 'ye'
            if country_name == 'Bolivia':
                return 'bo'
            elif country_name == 'Congo, Rep.':
                return 'cg'
            elif country_name == 'Dominica':
                return 'do'
            elif country_name == 'Egypt, Arab Rep.':
                return 'eg'
            elif country_name == 'Iran, Islamic Rep.':
                return 'ir'
            elif country_name == 'Korea, Rep.':
                return 'kr'
            elif country_name == 'Kyrgyz Republic':
                return 'kg'
            elif country_name == 'Libya':
                return 'ly'
            elif country_name == 'Slovak Republic':
                return 'sk'
            elif country_name == 'Tanzania':
                return 'tz'
            elif country_name == 'Venezuela, RB':
                return 've'
            elif country_name == 'Vietnam':
                return 'vn'

    # If no country is found, return none
    return None
