import pickle

with open("customers_db.bin", "rb") as db_file:
    db = pickle.load(db_file)

print(db)
