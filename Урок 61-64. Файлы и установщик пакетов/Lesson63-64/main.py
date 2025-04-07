# ==============================================LESSON63==============================================
# Установщик пакетов pip. Использование API.
# https://openweathermap.org/
# Регистрация и получение API-key
# py -m pip --version
# echo %PATH% и найти Python\Scripts
# setx PATH "%PATH%; C:\Python\Scripts"
# pip install requests
# pip uninstall requests
# https://openweathermap.org/current  zeynalov_f@itstep.academy
# https://openweathermap.org/forecast5


# from datetime import datetime
# import requests
#
# # current = datetime.datetime.now()
# # print(current)
# # print(current.year, current.month, current.day, current.hour, current.minute)
#
# # print(current)
# # print(current + datetime.timedelta(days=5))
#
#
# API_KEY = "6d8e5d0eb1cfe35d19dd82f286959e87"
# BASE_WEATHER_URL = f"https://api.openweathermap.org/data/2.5/weather?appid={API_KEY}"
# CITY = "Baku"
#
# url = f"{BASE_WEATHER_URL}&q={CITY}&units=metric"
# response = requests.get(url).json()
# print(response)
#
#
# current_datetime = datetime.now()
# temperature_celsius = response["main"]["temp"]
# temperature_celsius_feels = response["main"]["feels_like"]
# humidity = response["main"]["humidity"]
# wind_speed = response["wind"]["speed"]
# weather_description = response["weather"][0]["description"]
# sunrise_time = datetime.fromtimestamp(response["sys"]["sunrise"]).time()
# sunset_time = datetime.fromtimestamp(response["sys"]["sunset"]).time()
#
# print(f"Datetime is: {current_datetime}")
# print(f"Temperature in {CITY} is {temperature_celsius:.2f}°C")
# print(f"Temperature in {CITY} feels like {temperature_celsius_feels:.2f}°C")
# print(f"Humidity in {CITY} is {humidity}%")
# print(f"Wind speed in {CITY} is {wind_speed}m/s")
# print(f"General Weather in {CITY} is {weather_description}")
# print(f"Sun rises in {CITY} at {sunrise_time} local time")
# print(f"Sun sets in {CITY} at {sunset_time} local time")
# print()

# ====================================================================================================
# from datetime import datetime
# import requests
#
# API_KEY = "6d8e5d0eb1cfe35d19dd82f286959e87"
# BASE_WEATHER_URL = f"https://api.openweathermap.org/data/2.5/forecast?appid={API_KEY}&lang=ru"
# CITY = "Baku"
#
# url = f"{BASE_WEATHER_URL}&q={CITY}&units=metric"
# response = requests.get(url).json()
# # print(url)
# # print(response)
#
#
# print(CITY)
# for elem in response["list"]:
#     print(datetime.fromtimestamp(elem["dt"]))
#     print(elem["main"]["temp"], "градусов по цельсию")
#     print(elem["wind"]["speed"], "м/с")
#     print(elem["weather"][0]["description"])
#     print()

# ==============================================LESSON64==============================================
# https://www.exchangerate-api.com/docs/overview

# from datetime import datetime
# import requests
#
# API_KEY = "85a6a5243c259f6497547dd7"
# BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest"
# CURRENT_CURRENCY = "USD"
# TARGET_CURRENCY = "RUB"
#
# url = f"{BASE_URL}/{CURRENT_CURRENCY}"
# response = requests.get(url).json()
# print(response)
#
# rate = response["conversion_rates"][TARGET_CURRENCY]
# last_upd = datetime.fromtimestamp(response["time_last_update_unix"])
#
# print(f"Last update: {last_upd}")
# print(f"From {CURRENT_CURRENCY} to {TARGET_CURRENCY} rate: {rate}")
