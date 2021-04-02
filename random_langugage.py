from random import randint


class RandomLanguage():
    """ Random language class for 'rand_language_repos.pyä """

    def __init__(self):
        """ Initialize class attributes """
        self.initialize_language_attributes()

    def initialize_language_attributes(self):
        """ Sets all right attributes for the random language. """

        languages = ['python', 'javascript',
                     'ruby', 'java', 'haskell', 'go', 'c']
        language_titles = ['Python', 'JavaScript',
                           'Ruby', 'Java', 'Haskell', 'GO', 'C']
        colors = ['#3776ab', '#f7df1e', '#e0115f',
                  '#339999', '#797979', '#00a7d0', '#3744a7']

        random_index = randint(0, len(languages)-1)

        self.language = languages[random_index]
        self.language_title = language_titles[random_index]
        self.language_color = colors[random_index]
