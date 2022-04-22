'''
This converst from one currency to another.
Note that only 4 currencies were used here and an assumed value assigned to each of them
NGN => Nigerian Naira
USD => USDollar
EUR => Euro
GPB => Pounds
'''
def currency():
    print("WELCOME TO THE CURRENCY CONVERTER\nPlease note that only Four currencies are considered here."
      "\nEnter 'NGN' for Naira, 'USD' for Dollar, 'EUR' for Euro and GBP for Pounds")

    curr_dict = {
        'NGN': 1, #NGN, we are using the naira as a base currency here, hence it was assigned a value of 1
        'USD': 550, #USD,
        'EUR': 620, #EUR,
        'GBP': 700, #GBP
    }
    #a function for the currency conversion
    def num():
        while True: #this will keep running until the user inputs an integer
            try: #checks for the user input, the user is supposed to input a number only
                amount = int(input(f'Enter amount in {cur_from}: '))
            except:
                print('Invalid Input, please enter a number!!!')
            else:
                break
        a = curr_dict.get(cur_from)
        b = curr_dict.get(cur_to)
        # a and b are the values of the keys(cur_from and cur_to) fro the dictionary
        conv_amount = (a * amount) / b #the conversion arithmetics
        print(f'{amount} {cur_from} = {conv_amount:1.6} {cur_to}')

    #the input
    curr = ['NGN', 'USD', 'EUR', 'GBP'] #a list of the available currencies
    cur_from = input('From: ').upper()
    cur_to = input('To: ').upper()
    #to check if the user input currencies are in the currency list
    if cur_from and cur_to in curr:
        num()
    else:
        print("Invalid currency")
#currency()