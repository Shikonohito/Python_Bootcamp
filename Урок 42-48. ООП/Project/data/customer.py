from data.bank_card import BankCard


class Customer:
    __f_name = "Unknown"
    __l_name = "Unknown"
    __m_name = "Unknown"
    __cards = list()

    def __init__(self, f_name: str, l_name: str, m_name: str, *cards: BankCard):
        self.__f_name = f_name
        self.__l_name = l_name
        self.__m_name = m_name
        self.__cards = list(cards)

    def add_card(self, card: BankCard):
        self.__cards.append(card)

    def __str__(self):
        result = "{}, {}, {}".format(self.__f_name, self.__l_name, self.__m_name)
        for card in self.__cards:
            result += " " + str(card)
        return result

    def get_cards(self):
        return self.__cards

    def set_card(self, *cards: BankCard):
        self.__cards = list(cards)

    def get_f_name(self):
        return self.__f_name

    def set_f_name(self, f_name: str):
        self.__f_name = f_name

    def get_l_name(self):
        return self.__l_name

    def set_l_name(self, l_name: str):
        self.__l_name = l_name

    def get_m_name(self):
        return self.__m_name

    def set_m_name(self, m_name: str):
        self.__m_name = m_name
