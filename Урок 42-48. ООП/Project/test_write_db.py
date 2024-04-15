import pickle
from data.bank_card import BankCard
from data.customer import Customer
from data.customer_db import CustomerDB

db = CustomerDB()

card_1 = BankCard("1111111111111111", "aaa", "bbb", "ccc", 9, 2025, "123")
card_2 = BankCard("2222222222222222", "aaa", "bbb", "ccc", 2, 2027, "124")
customer_1 = Customer("aaa", "bbb", "ccc", card_1, card_2)

card_3 = BankCard("3333333333333333", "AAA", "BBB", "CCC", 5, 2026, "345")
customer_2 = Customer("AAA", "BBB", "CCC", card_3)

db.add_customer(customer_1, customer_2)

with open("customers_db.bin", "wb") as db_file:
    pickle.dump(db, db_file)
