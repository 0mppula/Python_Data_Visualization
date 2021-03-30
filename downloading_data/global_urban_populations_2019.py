import csv
import pygal
from pygal.style import DarkenStyle, LightColorizedStyle, RotateStyle

from country_codes import get_country_code

# Urban population Data
# urban_pop_2019 = './data/urban_population_2019.csv'
urban_pop_2019 = './downloading_data/data/urban_population_2019.csv'
cc_urban_pop = {}
cc_error = {}

with open(urban_pop_2019) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    cc_urban_pop_1, cc_urban_pop_2, cc_urban_pop_3 = {}, {}, {}
    for row in reader:
        try:
            country_name = row[0]
            urban_pop = int(row[63])
            code = get_country_code(country_name)

        except ValueError:
            print(f'ERROR: {country_name}')

        else:
            if code:
                cc_urban_pop[code] = urban_pop
            else:
                cc_error[country_name] = urban_pop

        # Group data into 3 groups
        for cc, urban_pop in cc_urban_pop.items():
            if urban_pop < 10**6:
                cc_urban_pop_1[cc] = urban_pop
            elif urban_pop < 10**7:
                cc_urban_pop_2[cc] = urban_pop
            else:
                cc_urban_pop_3[cc] = urban_pop


wm = pygal.maps.world.World()
wm.add('<1M', cc_urban_pop_1)
wm.add('<10M', cc_urban_pop_2)
wm.add('>10M', cc_urban_pop_3)

wm.render_to_file(
    'downloading_data/images/svg/world_urban_population_2019.svg')
