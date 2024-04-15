class BankCard:
    __id = "0000000000000000"
    __f_name = "Unknown"
    __l_name = "Unknown"
    __m_name = "Unknown"
    __month = 1
    __year = 1900
    __code = "000"

    def __init__(self, card_id: str, f_name: str, l_name: str, m_name: str, month: int, year: int, code: str):
        self.__id = card_id
        self.__f_name = f_name
        self.__l_name = l_name
        self.__m_name = m_name
        self.__month = month
        self.__year = year
        self.__code = code

    def __str__(self):
        return "{}, {}, {}, {}, {}, {}, {}".format(self.__id, self.__f_name, self.__l_name,
                                                   self.__m_name, self.__month, self.__year, self.__code)

    def get_id(self):
        return self.__id

    def get_f_name(self):
        return self.__f_name

    def get_l_name(self):
        return self.__l_name

    def get_m_name(self):
        return self.__m_name

    def get_month(self):
        return self.__month

    def get_year(self):
        return self.__year

    def get_code(self):
        return self.__code
