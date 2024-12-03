from datetime import datetime


class BankCard:
    """
    The BankCard class represents a bank card with attributes such as card ID, first name, last name, expiration date, and balance.
    """
    __card_id = "0000000000000000"
    __f_name = "Unknown"
    __l_name = "Unknown"
    __month = datetime.now().month
    __year = datetime.now().year + 3
    __balance = 0

    def __init__(self, card_id: str, f_name: str, l_name: str,
                 month=datetime.now().month, year=datetime.now().year + 3, balance=0.0):
        """
        This method serves as the constructor for the BankCard class. It initializes a new instance of the BankCard class with the provided parameters:
        :param card_id: The unique identifier of the bank card.
        :param f_name: The first name associated with the bank card.
        :param l_name: The last name associated with the bank card.
        :param month: The expiration month of the bank card. Defaults to the current month if not provided.
        :param year: The expiration year of the bank card. Defaults to the current year plus three years if not provided.
        :param balance: The initial balance associated with the bank card. Defaults to 0.0 if not provided.
        """
        self.set_card_id(card_id)
        self.set_f_name(f_name)
        self.set_l_name(l_name)
        self.set_month(month)
        self.set_year(year)
        self.set_balance(balance)

    def set_card_id(self, card_id: str):
        """
        Sets the card ID of the bank card.
        :param card_id: The new card ID to be set.
        If the provided card ID is a string of 16 digits, it sets the card ID of the bank card to the provided value.
        If the provided card ID does not meet the criteria, the card ID remains unchanged.
        """
        if len(card_id) == 16 and card_id.isdigit():
            self.__card_id = card_id

    def get_card_id(self):
        """
        Retrieves the card ID.

        :return: A string representing the 16-digit card number.
        """
        return self.__card_id

    def set_f_name(self, f_name: str):
        """
        Sets the first name of the cardholder if it consists only of alphabetic characters.

        :param f_name: A string representing the first name of the cardholder.
        """
        if f_name.isalpha():
            self.__f_name = f_name

    def get_f_name(self):
        """
        Retrieves the first name of the cardholder.

        :return: A string representing the first name of the cardholder.
        """
        return self.__f_name

    def set_l_name(self, l_name: str):
        """
        Sets the last name of the cardholder if it consists only of alphabetic characters.

        :param l_name: A string representing the last name of the cardholder.
        """
        if l_name.isalpha():
            self.__l_name = l_name

    def get_l_name(self):
        """
        Retrieves the last name of the cardholder.

        :return: A string representing the last name of the cardholder.
        """
        return self.__l_name

    def set_month(self, month: int):
        """
        Sets the expiration month if it is between 1 and 12.

        :param month: An integer representing the expiration month.
        """
        if 1 <= month and month <= 12:
            self.__month = month

    def get_month(self):
        """
        Retrieves the expiration month.

        :return: An integer representing the expiration month.
        """
        return self.__month

    def set_year(self, year: int):
        """
        Sets the expiration year if it is not earlier than 1900.

        :param year: An integer representing the expiration year.
        """
        if 1900 <= year:
            self.__year = year

    def get_year(self):
        """
        Retrieves the expiration year.

        :return: An integer representing the expiration year.
        """
        return self.__year

    def set_balance(self, balance: float):
        """
        Sets the current balance on the card if it is greater than 0.

        :param balance: A float representing the current balance.
        """
        if balance > 0:
            self.__balance = balance

    def get_balance(self):
        """
        Retrieves the current balance on the card.

        :return: A float representing the current balance.
        """
        return self.__balance

    def __str__(self):
        """
        Returns a string representation of the BankCard object.

        :return: A string containing card details.
        """
        return f"{self.__card_id} {self.__f_name} {self.__l_name} {self.__month}/{self.__year} {self.__balance}"

    def top_up(self, balance: float):
        """
        Adds funds to the card balance if the provided amount is positive.

        :param balance: A float representing the amount to be added.
        :return: True if the top-up was successful, False otherwise.
        """
        is_success = False
        if balance > 0:
            self.__balance += balance
            is_success = True
        return is_success

    def withdraw(self, balance: float):
        """
        Deducts funds from the card balance if the provided amount is positive and available.

        :param balance: A float representing the amount to be deducted.
        :return: True if the withdrawal was successful and the balance is sufficient, False otherwise.
        """
        is_success = False
        if balance > 0 and self.__balance > balance:
            self.__balance -= balance
            is_success = True
        return is_success

    def is_expired(self):
        """
        Checks if the card has expired based on the current date.

        :return: True if the card is expired, False otherwise.
        """
        now_year = datetime.now().year
        return self.__year < now_year or (self.__year == now_year and self.__month > datetime.now().month)