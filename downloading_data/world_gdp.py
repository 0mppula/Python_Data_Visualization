import json
import pygal
from pygal.style import DarkenStyle

from country_codes import get_country_code

# GDP data file
gdp_data = './downloading_data/data/global_gdp.json'
# gdp_data = './data/global_gdp.json'

# GDP Dictionary
cc_gdp = {}
cc_no_data = {}

with open(gdp_data) as f:
    data = json.load(f)

    for pop_dict in data:
        if pop_dict['Year'] == '2010':
            country_name = pop_dict['Country Name']
            gdp = int(float(pop_dict['Value']))
            code = get_country_code(country_name)

            if code:
                cc_gdp[code] = gdp
            else:
                cc_no_data[country_name] = gdp
                print(f'ERROR: {country_name}, not data.')

            cc_gdp_1, cc_gdp_2, cc_gdp_3 = {}, {}, {}
            for cc, gdp in cc_gdp.items():
                if gdp < 10**10:  # under 100 billion
                    cc_gdp_1[cc] = gdp
                elif gdp < 10**11:  # under 1 trillion
                    cc_gdp_2[cc] = gdp
                else:               # over 1 trillion
                    cc_gdp_3[cc] = gdp

# Plot data with pygal world
wm_style = DarkenStyle('#ff8723')
wm = pygal.maps.world.World(style=wm_style)
wm.title = ('Global GDP (in Billions $USD) - 2010')
wm.add('<$100B', cc_gdp_1)
wm.add('<$1000B', cc_gdp_2)
wm.add('>$1000B', cc_gdp_3)

wm.render_to_file('downloading_data/images/svg/global_gdp_2010.svg')
