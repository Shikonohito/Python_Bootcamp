from data.bank_card import BankCard
from data.customer import Customer


class CustomerDB:
    __customers = list()

    def __init__(self, *customers: Customer):
        self.__customers = list(customers)

    def __str__(self):
        str_data = ""
        if len(self.__customers) > 0:
            str_data = str(self.__customers[0])
            for i in range(1, len(self.__customers)):
                str_data += "\n" + str(self.__customers[i])
        return str_data

    def add_customer(self, *customer: Customer):
        for cust in customer:
            self.__customers.append(cust)
