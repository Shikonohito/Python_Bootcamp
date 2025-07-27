from datetime import datetime, timedelta

def create_base_customer():
    customer_id = "SOME_ID"
    customer_name = "SOME_NAME"
    customer_balance = 9999
    customer_subscribe_status = False
    customer_subscribe_date = datetime.now().date()
    return [customer_id, customer_name, customer_balance, customer_subscribe_status, customer_subscribe_date]

def init_test_customers():
    customer_1 = create_base_customer()
    customer_1[0] = "C-0045".upper()
    customer_1[1] = "Teston".capitalize()
    customer_1[2] = 2500
    customer_1[3] = True
    new_date = (datetime.now() + timedelta(days=30)).date()
    customer_1[4] = new_date
    if new_date < datetime.now().date():
        customer_1[3] = False

    customer_2 = create_base_customer()
    customer_2[0] = "C-0055".upper()
    customer_2[1] = "Bob".capitalize()
    customer_2[2] = 54
    customer_2[3] = True
    new_date = datetime.now().date()
    customer_2[4] = new_date
    if new_date < datetime.now().date():
        customer_2[3] = False

    customer_3 = create_base_customer()
    customer_3[0] = "C-0065".upper()
    customer_3[1] = "Kate".capitalize()
    customer_3[2] = 0
    customer_3[3] = True
    new_date = (datetime.now() - timedelta(days=30)).date()
    customer_3[4] = new_date
    if new_date < datetime.now().date():
        customer_3[3] = False
    return [customer_1, customer_2, customer_3]

def get_customer_index(customers: list[list], customer_id: str):
    index = -1
    for i in range(len(customers)):
        if customers[i][0] == customer_id:
            index = i
            break
    return index

def get_customer(customers: list[list], customer_id: str):
    found_customer = None
    index = get_customer_index(customers, customer_id)
    if index != -1:
        found_customer = customers[index]
    return found_customer

def subscribe_customer(customer: list, month: int):
    subscribe_status = customer[3]
    total_days = month * 30
    subscribe_end_date = customer[4]
    if subscribe_status:
        subscribe_end_date += timedelta(days=total_days)
    else:
        subscribe_end_date = datetime.now() + timedelta(days=total_days)
    customer[3] = True
    customer[4] = subscribe_end_date
    if subscribe_end_date < datetime.now().date():
        customer[3] = False
