from currency_converter import currency
from temperature_converter import temperature
from basic import time, lenght, weight

def conversion():
    conv = input("What conversion do you want to perform (Lenght, Weight, Currency, Temperature or Time):\n").lower()
    if conv == "lenght":
        lenght()
    elif conv == "weight":
        weight()
    elif conv == "time":
        time()
    elif conv == "temperature":
        temperature() #from temp_converter import temperature
    elif conv == "currency":
        currency()
    else:
        print("Please choose between lenght, weight, currency, temperature and time.")

count = 0
while count >= 0:
    act = input("Do you want to perform a conversion? Yes/No: ").lower()
    if act == "yes" or act == "y":
        conversion()
    elif act == "no" or act == "n":
        print("Thank you for using the conversion")
        break
    else:
        pass