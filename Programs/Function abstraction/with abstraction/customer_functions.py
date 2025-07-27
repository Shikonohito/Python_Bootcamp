from datetime import datetime, timedelta

def set_customer_id(customer: list, new_id: str):
    customer[0] = new_id.upper()

def set_customer_name(customer: list, new_name: str):
    customer[1] = new_name.capitalize()

def set_customer_balance(customer: list, new_balance: int):
    customer[2] = new_balance

def set_customer_subscribe_date(customer: list, new_date=datetime.now().date()):
    customer[3] = True
    customer[4] = new_date
    if new_date < datetime.now().date():
        customer[3] = False

def create_base_customer():
    customer_id = "SOME_ID"
    customer_name = "SOME_NAME"
    customer_balance = 9999
    customer_subscribe_status = False
    customer_subscribe_date = datetime.now().date()
    return [customer_id, customer_name, customer_balance, customer_subscribe_status, customer_subscribe_date]

def init_test_customers():
    customer_1 = create_base_customer()
    set_customer_id(customer_1, "C-0045")
    set_customer_name(customer_1, "Teston")
    set_customer_balance(customer_1, 2500)
    set_customer_subscribe_date(customer_1, (datetime.now() + timedelta(days=30)).date())

    customer_2 = create_base_customer()
    set_customer_id(customer_2, "C-0055")
    set_customer_name(customer_2, "Bob")
    set_customer_balance(customer_2, 54)
    set_customer_subscribe_date(customer_2, datetime.now().date())

    customer_3 = create_base_customer()
    set_customer_id(customer_3, "C-0065")
    set_customer_name(customer_3, "Kate")
    set_customer_balance(customer_3, 0)
    set_customer_subscribe_date(customer_3, (datetime.now() - timedelta(days=30)).date())

    return [customer_1, customer_2, customer_3]

def get_customer_id(customer: list):
    return customer[0]

def get_customer_name(customer: list):
    return customer[1]

def get_customer_balance(customer: list):
    return customer[2]

def get_customer_subscribe_status(customer: list):
    return customer[3]

def get_customer_subscribe_end_date(customer: list):
    return customer[4]

def get_customer_index(customers: list[list], customer_id: str):
    index = -1
    for i in range(len(customers)):
        if get_customer_id(customers[i]) == customer_id:
            index = i
            break
    return index

def is_customer_duplicate(customers: list[list], customer_id: str):
    return get_customer_index(customers, customer_id) != -1

def get_customer(customers: list[list], customer_id: str):
    found_customer = None
    index = get_customer_index(customers, customer_id)
    if index != -1:
        found_customer = customers[index]
    return found_customer

def subscribe_customer(customer: list, month: int):
    subscribe_status = get_customer_subscribe_status(customer)
    total_days = month * 30
    subscribe_end_date = get_customer_subscribe_end_date(customer)
    if subscribe_status:
        subscribe_end_date += timedelta(days=total_days)
    else:
        subscribe_end_date = datetime.now() + timedelta(days=total_days)
    set_customer_subscribe_date(customer, subscribe_end_date)
