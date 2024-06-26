import pandas as pd
import sys


#The menu() function generates the UI the accepts and validates user choice
def menu():

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
        print("7. Trends & Patterns over time")
        print("")
        print("######################################################")

        
        menu_choice = input("Please enter the number of your choice (1-7): ")

        try:
            int(menu_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(menu_choice) < 1 or int(menu_choice) > 7:
                print("Sorry, you did not neter a valid choice")
                flag = True
            else:
                print("hit")
                return menu_choice  


#Gets the short version of the conversion information based on user menu choice
def get_currency ():
    currencies = {
       '1': 'GBP - EUR',
       '2': 'EUR - GBP', 
       '3': 'GBP - AUD',
       '4': 'AUD - GBP',
       '5': 'GPB - JPY',
       '6': 'JPY - GBP'}
   
    currency = currencies.get(menu_choice)
    
    return currency

def trends_menu():
    flag = True

    while flag:
        print("######################################################")
        print("Which trend/pattern would you like today?")
        print("1. Trend over time for the value of Pound Sterling(GBP) to US Dollar(USD)")
        print("2. Trend over time for the value of US Dollar to Pound Sterling(GBP)")
        print("3. Value trends for GBP-USD and USD-GBP (combined graph)")
        print("4. Austrailan Dollars (AUD) to Pound Sterling (GBP)")
        print("5. Value trends between two dates")
        print("######################################################")

        
        trend_choice = input("Please enter the number of your choice (1-7): ")

        try:
            int(trend_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(trend_choice) < 1 or int(trend_choice) > 5:
                print("Sorry, you did not neter a valid choice")
                flag = True
            else:
                return int(trend_choice)


menu_choice = menu()

if int(menu_choice) >= 1 and int(menu_choice) < 7:
    print("hit")
    currency = get_currency()
elif int(menu_choice) == 7:
    #run the trends menu
    trend_choice = trends_menu()
    
    #we will need a complete dataframe for all the functions here
    df = pd.read_csv('Task4a_data.csv')
    
    if trend_choice == 1:
        print("Option 1 Selected")
    elif trend_choice == 2:
        print("Option 2 Selected")
    elif trend_choice == 3:
        print("Option 3 Selected")
    elif trend_choice == 4:
        print("Option 4 Selected")
    elif trend_choice == 5:
        print("Option 5 Selected")
    else:
        print("Please choose a valid option")
    
    #system close
    sys.exit()



#The get_conversion_rate function uses pandas to get the latest conversion rate
#Imports a csv file in to a data frame
#Uses 'iloc' to get the last/most recent value in the selected column

def get_conversion_rate():
    df = pd.read_csv("Task4a_data.csv")
    
    conversion_rate = round(df[currency].iloc[-1],2)


    return conversion_rate

conversion_rate = get_conversion_rate()


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

conversion_amount = float(get_amount_to_convert())

#Performs the converison and outputs the final values
def perfom_conversion():
    amount_recieved = round(conversion_amount * conversion_rate, 2)

    print("##################################")
    print('You are converting {} in {}'.format(conversion_amount, currency[0:3]) )
    print('You will recieve {} in {}'.format(amount_recieved, currency[6:9]))
    
perfom_conversion()