import unittest

from country_codes import get_country_code


class TestCountryCodes(unittest.TestCase):
    """ Tests for 'country_codes.py'. """

    def test_country_code(self):
        """ Does the program return the right country codes. """

        country_code = get_country_code('Finland')
        self.assertEqual(country_code, 'fi')

        country_code = get_country_code('United Arab Emirates')
        self.assertEqual(country_code, 'ae')

        country_code = get_country_code('Sweden')
        self.assertEqual(country_code, 'se')

        country_code = get_country_code('Lebanon')
        self.assertEqual(country_code, 'lb')


unittest.main()
