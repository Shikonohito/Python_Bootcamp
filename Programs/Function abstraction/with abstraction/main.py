# Пример использования абстракции на функциях
from customer_functions import *

def customer_to_str(customer: list):
    result = f"{get_customer_id(customer)} {get_customer_name(customer)} {get_customer_balance(customer)}"
    if get_customer_subscribe_status(customer):
        result += f" {get_customer_subscribe_end_date(customer)}"
    else:
        result += " Отсутствует"
    return result

def print_all_customers(customer_list: list[list]):
    for customer in customer_list:
        print(customer_to_str(customer))

def register_new_customer(customer_list: list[list]):
    status_code = 0
    input_id = input("Введите новый идентификатор клиента: ")
    while is_customer_duplicate(customer_list, input_id) and input_id:
        print("Клиент с указанным идентификатором уже присутствует.")
        input_id = input("Пожалуйста введите другой идентификатор клиента: ")

    if not input_id:
        status_code = -1

    if not status_code:
        print("=" * 80)
        input_name = input("Введите имя клиента: ")
        if not input_name:
            status_code = -2

    if not status_code:
        is_correct_balance = False
        print("=" * 80)
        input_balance = input("Введите баланс клиента: ")
        if not input_balance:
            status_code = -3
        else:
            input_balance = int(input_balance)
            if input_balance >= 0:
                is_correct_balance = True

        while not is_correct_balance and not status_code:
            print("Баланс не может быть отрицательным.")
            input_balance = input("Пожалуйста введите положительный баланс: ")
            if not input_balance:
                status_code = -3
                break
            input_balance = int(input_balance)
            if input_balance >= 0:
                is_correct_balance = True

    print("=" * 80)
    if not status_code:
        new_customer = create_base_customer()
        set_customer_id(new_customer, input_id)
        set_customer_name(new_customer, input_name)
        set_customer_balance(new_customer, input_balance)
        set_customer_subscribe_date(new_customer)
        customer_list.append(new_customer)
        print("Новый клиент успешно зарегистрирован.")
    elif status_code == -1:
        print("Регистрация нового клиента прервана на введении идентификатора.")
    elif status_code == -2:
        print("Регистрация нового клиента прервана на введении имени.")
    elif status_code == -3:
        print("Регистрация нового клиента прервана на введении баланса.")

def subscribe_menu(customer: list):
    subscribe_per_day_price = 5
    print(f"Курс подписки: 1 месяц = {subscribe_per_day_price}")
    input_month = input("Введите количество месяцев: ")
    if not input_month:
        print("Оформление подписки прервано на вводе количества месяцев.")
    else:
        input_month = int(input_month)
        if input_month < 1:
            input_month = 0
            while not input_month:
                print("Месяц не может быть меньше 1")
                input_month = input("Пожалуйста введите корректный месяц: ")
                if not input_month:
                    print("Оформление подписки прервано на вводе количества месяцев.")
                    break
                input_month = int(input_month)
                if input_month < 1:
                    input_month = 0
        to_pay = subscribe_per_day_price * input_month
        balance = get_customer_balance(customer)
        print("=" * 80)
        print(f"На балансе клиента {balance}")
        print(f"Для оформления подписки на {input_month} месяцев потребуется заплатить {to_pay}.")
        balance_after_pay = balance - to_pay
        if balance_after_pay < 0:
            print("На балансе клиента недостаточно денег.")
            input_month = balance // subscribe_per_day_price
            to_pay = subscribe_per_day_price * input_month
            balance_after_pay = balance - to_pay
            print(f"Можно оформить подписку на {input_month} месяцев. Потребуется заплатить {to_pay}.")

        if input("Подтвердите оформление подписки (Y/N): ").upper() == "Y":
            set_customer_balance(customer, balance_after_pay)
            subscribe_customer(customer, input_month)
        else:
            print("Оформление подписки прервано на подтверждении оформления подписки.")

def select_customer(customer_list: list[list]):
    input_cust_id = input("Введите идентификатор клиента: ")
    selected_customer = get_customer(customer_list, input_cust_id)
    if not selected_customer:
        print("Клиент с указанным идентификатором отсутствует.")
    else:
        while True:
            print(customer_to_str(selected_customer))
            print("1. Оформить подписку клиенту")
            print("2. Вернуться")
            choice = input("Выберите действие: ")
            if choice == "1":
                print("=" * 80)
                subscribe_menu(selected_customer)
                print("=" * 80)
            elif choice == "2":
                break
            else:
                print("Выбрано неверное действие.")


customers = init_test_customers()

while True:
    print("1. Показать данные всех клиентов")
    print("2. Зарегистрировать нового клиента")
    print("3. Выбрать клиента")
    print("4. Завершить программу")
    choice = input("Выберите действие: ")
    if choice == "1":
        print("=" * 80)
        print_all_customers(customers)
        print("=" * 80)
    elif choice == "2":
        print("=" * 80)
        register_new_customer(customers)
        print("=" * 80)
    elif choice == "3":
        print("=" * 80)
        select_customer(customers)
        print("=" * 80)
    elif choice == "4":
        print("=" * 80)
        break
    else:
        print("Выбрано неверное действие.")


print("Завершение программы.")
