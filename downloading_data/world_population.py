import json
import pygal
from pygal.style import DarkenStyle

from country_codes import get_country_code


# Load json data into a list
filename = './downloading_data/data/population_data.json'

# Build the data into a list
cc_populations = {}
cc_missing = []
with open(filename) as f:
    pop_data = json.load(f)

    # Print the 2010 population for each country
    for pop_dict in pop_data:
        if pop_dict['Year'] == '2010':
            country_name = pop_dict['Country Name']
            population = int(float(pop_dict['Value']))
            code = get_country_code(country_name)

            if code:
                cc_populations[code] = population
            else:
                print(f'ERROR: {country_name}')
                cc_missing.append(country_name)

            # Group contries into 3 population levels
            cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
            for cc, pop in cc_populations.items():
                if pop < 10000000:
                    cc_pops_1[cc] = pop  # under 1 million
                elif pop < 1000000000:
                    cc_pops_2[cc] = pop  # under 1 billion
                else:
                    cc_pops_3[cc] = pop  # over 1 billion


wm_style = DarkenStyle('#ee2222')
wm = pygal.maps.world.World(style=wm_style)
wm.title = ('World population in 2010, by Country')
wm.add('0-10m', cc_pops_1)
wm.add('10-1b', cc_pops_2)
wm.add('>10b', cc_pops_3)

wm.render_to_file('downloading_data/images/svg/world_population_2010.svg')
