class Result:
    __contents = dict()

    PROPERTIES = ['ID', 'COUNTRY', 'YEAR', 'RANK', 'SCORE', 'GDP']

    def __init__(self):
        self.__contents.update('id', None)
        self.__contents.update('country', None)
        self.__contents.update('year', None)
        self.__contents.update('rank', None)
        self.__contents.update('score', None)
        self.__contents.update('gdp', None)

    def __init__(self, tupple_result):
        self.__contents['id'] = tupple_result[0]
        self.__contents['year'] = tupple_result[1]
        self.__contents['country'] = tupple_result[2]
        self.__contents['rank'] = tupple_result[3]
        self.__contents['score'] = tupple_result[4]
        self.__contents['gdp'] = tupple_result[5]



        return return_str

    def set_id(self, id):
        self.__contents.update('id', id)

    def set_country(self, country_name):
        self.__contents.update('country', country_name)

    def set_year(self, year):
        self.__contents.update('year', year)

    def set_rank(self, rank):
        self.__contents.update('rank', rank)

    def set_score(self, score):
        self.__contents.update('score', score)

    def set_gdp(self, gdp):
        self.__contents.update('gdp', gdp)

    def get_id(self):
        return self.__contents['id']

    def get_country(self):
        return self.__contents['country']

    def get_year(self):
        return self.__contents['year']

    def get_rank(self):
        return self.__contents['rank']

    def get_score(self):
        return self.__contents['score']

    def get_gdp(self):
        return self.__contents['gdp']
