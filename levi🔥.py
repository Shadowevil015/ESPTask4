import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def menu():
    flag = True

    while flag:
        print("######################################################")
        print("Hello, welcome to RBSX group!")
        print("What would you like to do?")
        print("1. Convert between currencies")
        print("2. See trends between GBP and USD")
        print("######################################################")

        menu_choice = input("Please enter the number of your choice (1-2): ")

        try:
            int(menu_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(menu_choice) < 1 or int(menu_choice) > 2:
                print("Sorry, you did not neter a valid choice")
                flag = True
            else:
                return menu_choice

#The menu() function generates the UI the accepts and validates user choice
def menu_conversion():
    
    flag = True

    while flag:

        print("######################################################")
        print("Which conversion would you like to make today?")
        print("1. Pound Sterling (GBP) to Euros (EUR)")
        print("2. Euros (EUR) to Pound Sterling(GBP)")
        print("3. Pound (GBP) to Austrailan Dollars (AUD)")
        print("4. Austrailan Dollars (AUD) to Pound Sterling (GBP)")
        print("5. Pound Sterling (GBP) to Japanese Yen (JPY)")
        print("6. Japanese Yen (JPY) to Pound Sterling (GBP)")
        print("######################################################")

        
        menu_choice = input("Please enter the number of your choice (1-6): ")

        try:
            int(menu_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(menu_choice) < 1 or int(menu_choice) > 6:
                print("Sorry, you did not neter a valid choice")
                flag = True
            else:
                return menu_choice  

def menu_trends():
    flag = True
    while flag:

        print("######################################################")
        print("What trends would you like to see?")
        print("1. GBP to USD conversion")
        print("2. USD to GBP conversion")
        print("######################################################")

        menu_choice = input("Please enter the number of your choice (1-2): ")

        try:
            int(menu_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(menu_choice) < 1 or int(menu_choice) > 6:
                print("Sorry, you did not neter a valid choice")
                flag = True
            else:
                return menu_choice 

#Gets the short version of the conversion information based on user menu choice
def get_currency ():
    currencies = {
       '1': 'GBP - EUR',
       '2': 'EUR - GBP', 
       '3': 'GBP - AUD',
       '4': 'AUD - GBP',
       '5': 'GPB - JPY',
       '6': 'JPY - GBP'
       }
   
    currency = currencies.get(menu_choice)
    
    return currency

#The get_conversion_rate function uses pandas to get the latest conversion rate
#Imports a csv file in to a data frame
#Uses 'iloc' to get the last/most recent value in the selected column
def get_conversion_rate():
    df = pd.read_csv("Task4a_data.csv")
    
    conversion_rate = round(df[currency].iloc[-1],2)


    return conversion_rate

#Accepts and validates user input for teh amount they want to convert
def get_amount_to_convert():
    print("You are converting: ",currency)
    
    flag = True
    
    while flag:
        conversion_amount = input("please enter the amount you wish to convert")
    
        try:
            float(conversion_amount)
        except:
            print("Sorry, you must enter a numerical value")
            flag = True
        else:
            return conversion_amount  

#Performs the converison and outputs the final values
def perfom_conversion():
    amount_recieved = round(conversion_amount * conversion_rate, 2)

    print("##################################")
    print('You are converting {} in {}'.format(conversion_amount, currency[0:3]) )
    print('You will recieve {} in {}'.format(amount_recieved, currency[6:9]))

def get_graph():
    # this function is used to generate the graph based on the user choice
    df = pd.read_csv("Task4a_data.csv")
    if menu_choice == "1": # GBP to USD graph
        conversion = 'GBP - USD'
    else: # USD to GBP, if any errors will display this anyway to avoid crashes
        conversion = 'USD - GBP'

    sns.lineplot(x="Date", y=conversion, data=df)
    plt.show()

mode = menu()
if mode == '1':
    menu_choice = menu_conversion()
    currency = get_currency()
    conversion_rate = get_conversion_rate()
    conversion_amount = float(get_amount_to_convert())
    perfom_conversion()
elif mode == '2':
    menu_choice = menu_trends()
    graph = get_graph()
