def temperature():
    print("WELCOME TO TEMPERATURE CONVERTER\nPlease enter only the first letter of the temperature.")
    temp_from1 = input('Temperature from: ').upper()
    temp_to1 = input('Temperature to: ').upper()
    while True:
        try:
            temp = float(input('Temperature: '))

            if temp_from1 == 'C' and temp_to1 == 'F':
                result = ((9/5)* temp) + 32
                print(f'{temp} {temp_from1} is equal to {result:1.4} {temp_to1}')
            elif temp_from1 == 'F' and temp_to1 == 'C':
                result = (5/9)*(temp - 32)
                print(f'{temp} {temp_from1} is equal to {result:1.4} {temp_to1}')
            elif temp_from1 == 'C' and temp_to1 == 'K':
                result = temp + 273
                print(f'{temp} {temp_from1} is equal to {result:1.4} {temp_to1}')
            elif temp_from1 == 'K' and temp_to1 == 'C':
                result = temp - 273
                print(f'{temp} {temp_from1} is equal to {result:1.4} {temp_to1}')
            elif temp_from1 == 'F' and temp_to1 == 'K':
                result = ((5/9)*(temp - 32)) + 273
                print(f'{temp} {temp_from1} is equal to {result:1.4} {temp_to1}')
            elif temp_from1 == 'K' and temp_to1 == 'F':
                result = ((9/5)*(temp - 273)) + 32
                print(f'{temp} {temp_from1} is equal to {result:1.4} {temp_to1}')
            else:
                print('Math Error! Invalid Input')
        except:
            print("Invalid Input, Please enter a number.")
        break
#temperature()