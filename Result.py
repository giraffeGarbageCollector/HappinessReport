

class Result:
    __contents = dict()

    def __init__(self):
        self.__contents.update('id', None)
        self.__contents.update('year', None)
        self.__contents.update('rank', None)
        self.__contents.update('score', None)
        self.__contents.update('gdp', None)

    def set_id(self, id):
        self.__contents.update('id', id)

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

    def get_year(self):
        return self.__contents['year']

    def get_rank(self):
        return self.__contents['rank']

    def get_score(self):
        return self.__contents['score']

    def get_gdp(self):
        return self.__contents['gdp']
