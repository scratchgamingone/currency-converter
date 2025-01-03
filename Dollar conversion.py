#Convert USD to any currency

#will set the inputted currency to USD
USD = float(input("Enter in how many USD to convert: "))

#Will show the price
print("$", USD)

#functions that allow users to add to convert to other currency
def usd_to_japanese_yen(): #will convert it to Japanese yen
    japanese_yen= USD * 157.82
    print("$", USD, "is", japanese_yen, "Japanese Yen")
def usd_to_united_arab_emirates_dirham(): #will convert it to United Arab Emirates Dirham
    uae= USD * 3.67
    print("$", USD, "is", uae, "United Arab Emirates Dirham")
def usd_to_euro(): #will convert it to Euro
    euro= USD * 0.96
    print("$", USD, "is", euro, "Euro")
def usd_to_chinese_yuan(): #will convert it to Chinese Yen
    chinese_yen= USD * 7.30
    print("$", USD, "is", chinese_yen, "Chinese Yuan")
def usd_to_czech_koruna(): #will convert it to Czech Koruna
    czech_koruna= USD * 7.30
    print("$", USD, "is", czech_koruna, "Czech Koruna")


def user_input(): #Function for asking users to pick again
    global user_choice
    user_choice = int(input("Pick one to choose:  \n"
                        "1. Convert to Japanese yen\n"
                        "2. Convert to United Arab Emirates Dirham \n"
                        "3. Convert to Euro \n"
                        "4. Convert to Chinese Yuan \n"
                        "5. Convert to Czech Koruna \n"))


while_run = True #will set the while_run to true so that the game runs when user put in valid number


#The rest of the script will ask the user input

def exist(): #Exist the while loop within the while loop
    pass


while while_run:
    #will ask the user to input their choices
    user_input()

    #Will ask the user to choose again if it's out of range
    while user_choice<0 or user_choice>5:
        print("Not a valid pick.")
        user_input()
        exist()

    if user_choice == 1: #will convert it to japanese yen if user input the number 1
        usd_to_japanese_yen()
        while_run = False #ends the converter program

    elif user_choice ==2: #will convert it to UAE dirham
        usd_to_united_arab_emirates_dirham()
        while_run = False #ends the converter program

    elif user_choice ==3: #will convert it to Euro
        usd_to_euro()
        while_run = False #ends the converter program

    elif user_choice ==4: #will convert it to Chinese Yuan
        usd_to_chinese_yuan()
        while_run = False #ends the converter program

    elif user_choice ==5: #will convert it to Czech Koruna
        usd_to_czech_koruna()
        while_run = False #ends the converter program

print("Goodbye!") #Exist the game

#end the Dollar conversion project




