def time():
    print("TIME CONVERSION\nPlease Enter hour, minute or second")
    len_dict = {
        "minute": 1,
        "second": 60,
        "hour": 1/60
    }
    units = ["minute", "second", "hour"]
    unit_from = input("Unit from: ").lower()
    unit_to = input("Unit to: ").lower()
    if unit_from and unit_to in units:
        while True:
            try:
                num = float(input("Enter the number to convert: "))
                a = len_dict.get(unit_from)
                b = len_dict.get(unit_to)
                soln = (num * b) / a
                print(f"{unit_from.capitalize()}: {num}\n{unit_to.capitalize()}: {soln}")
                break
            except:
                print("Invalid, Please input a number.")
    else:
        print("Invalid input")



def lenght():
    print("LENGHT CONVERSION\nPlease Enter kilometer, meter, centimeter, millimeter. or inch")
    len_dict = {
        "m": 1,
        "mm": 1000,
        "cm": 100,
        "km": 0.001,
        "inch": 39.37
    }
    units = ["m", "km", "cm", "mm", "inch"]
    unit_from = input("Unit from: ").lower()
    unit_to = input("Unit to: ").lower()
    if unit_from and unit_to in units:
        while True:
            try:
                num = float(input("Enter the number to convert: "))
                a = len_dict.get(unit_from)
                b = len_dict.get(unit_to)
                soln = (num * b) / a
                print(f"{unit_from.capitalize()}: {num}\n{unit_to.capitalize()}: {soln}")
                break
            except:
                print("Invalid, Please input a number.")
    else:
        print("Invalid input")


def weight():
    print("WEIGHT CONVERSION\nPlease Enter milligram(mg), centigram(cg), gram(g) or kilogram(kg) ")
    len_dict = {
        "g": 1,
        "cg": 100,
        "kg": 0.001,
        "mg": 1000
    }
    units = ["g", "kg", "mg", "cg"]
    unit_from = input("Unit from: ").lower()
    unit_to = input("Unit to: ").lower()
    a = unit_from and unit_to in units
    print(a)
    if unit_from and unit_to in units:
        while True:
            try:
                num = float(input("Enter the number to convert: "))
                a = len_dict.get(unit_from)
                b = len_dict.get(unit_to)
                soln = (num * b) / a
                print(f"{unit_from.capitalize()}: {num}\n{unit_to.capitalize()}: {soln}")
                break
            except:
                print("Invalid, Please input a number.")
    else:
        print("Invalid input")