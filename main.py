import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 


#The menu() function generates the UI the accepts and validates user choice

def menu():

    flag = True

    while flag:
        
        print("Which conversion would you like to make today?")
        print("1. Pound Sterling (GBP) to Euros (EUR)")
        print("2. Euros (EUR) to Pound Sterling(GBP)")
        print("3. Pound (GBP) to Austrailan Dollars (AUD)")
        print("4. Austrailan Dollars (AUD) to Pound Sterling (GBP)")
        print("5. Pound Sterling (GBP) to Japanese Yen (JPY)")
        print("6. Japanese Yen (JPY) to Pound Sterling (GBP)")
        print("7. shows trend of GBP to USD conversion")
        print("8. shows trend of USD to GBP conversion")


        menu_choice = input("Please enter the number of your choice (1-8): ")

        try:
            int(menu_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(menu_choice) < 1 or int(menu_choice) > 8:
                print("Sorry, you did not neter a valid choice")
                flag = True
            else:
                return menu_choice  


def convert_GBP():
    GBP_USD = pd.read_csv("Task4a_data.csv")
    sns.lineplot( x="Date", y="GBP - USD", data=GBP_USD)
    plt.show()

def convert_USD():
    USD_GBP = pd.read_csv("Task4a_data.csv")
    sns.lineplot( x="Date", y="USD - GBP", data=USD_GBP)
    plt.show()



#Gets the short version of the conversion information based on user menu choice
def get_currency ():


    currencies = {
       '1': 'GBP - EUR',
       '2': 'EUR - GBP', 
       '3': 'GBP - AUD',
       '4': 'AUD - GBP',
       '5': 'GPB - JPY',
       '6': 'JPY - GPB'}

    currency = currencies.get(menu_choice)

    return currency

menu_choice = menu()


#The get_conversion_rate function uses pandas to get the latest conversion rate
#Imports a csv file in to a data frame
#Uses 'iloc' to get the last/most recent value in the selected column
def get_conversion_rate():
    df = pd.read_csv("Task4a_data.csv")

    conversion_rate = round(df[currency].iloc[-1],2)

    return conversion_rate



#Accepts and validates user input for the amount they want to convert
def get_amount_to_convert():
    print("You are converting: ",currency)

    flag = True

    while flag:
        conversion_amount = input("please enter the ammount you wish to convert")

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



def convert_GBP ():
    GBP_USD = pd.read_csv("Task4a_data.csv")
    sns.lineplot( x="Date", y="GBP - USD", data=GBP_USD)
    plt.show()

def convert_USD ():
    USD_GBP = pd.read_csv("Task4a_data.csv")
    sns.lineplot( x="Date", y="USD - GBP", data=USD_GBP)
    plt.show()

if menu_choice == "7":
    convert_GBP()
elif menu_choice =="8":
    convert_USD
else:
    currency = get_currency()
    conversion_rate = get_conversion_rate()
    conversion_amount = float(get_amount_to_convert())
    perfom_conversion()
    

