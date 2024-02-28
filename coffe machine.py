menu = {
    "espresso":{
        "ingrediants":{
            "water": 80,
            "coffee" : 18
        },       
        "cost" : 1.5
    },
    "latte":{
        "ingrediants":{
            "water": 200,
            "coffee" : 25,
            "milk" : 150
        },       
        "cost" : 2.5
    },
    "cappuccino":{
        "ingrediants":{
            "water": 100,
            "coffee" : 25,
            "milk" : 100
        },       
        "cost" : 3.0
    }
}
resources = {
    "water" : 300,
    "milk" : 200,
    "coffee" : 100
}

run = True

def coffee_making(user_choice,will_run):
    #print(menu[user_choice])
    print(f"Ingediants : {menu[user_choice]["ingrediants"]}")
    print(f"Cost : {menu[user_choice]["cost"]}")
    if menu[user_choice]["ingrediants"]["water"] < resources["water"] and menu[user_choice]["ingrediants"]["coffee"] < resources["coffee"]:
        will_run = True
    else:
        if menu[user_choice]["ingrediants"]["water"] > resources["water"]:
            print(f"water is short")
            #print(resources)
            print(f"water : {resources['water']}")
            print(f"coffee : {resources['coffee']}")
            print(f"milk : {resources['milk']}")
            will_run = False
        elif menu[user_choice]["ingrediants"]["coffee"] > resources["coffee"]:
            print(f"Coffee is short.")
            #print(resources)
            print(f"water : {resources['water']}")
            print(f"coffee : {resources['coffee']}")
            print(f"milk : {resources['milk']}")
            will_run = False
        elif menu[user_choice]["ingrediants"]["milk"] > resources["milk"]:
            print(f"Milk is short.")
            #print(resources)
            print(f"water : {resources['water']}")
            print(f"coffee : {resources['coffee']}")
            print(f"milk : {resources['milk']}")
            will_run = False
            
    return will_run
        
def money_calculation():
    quartar = int(input("How many quartars, 0.25 : "))
    dimes = int(input("How many dimes, 0.10 : "))
    nickles = int(input("How many Nickles, 0.05 : "))
    pennies = int(input("How many Penneis, 0.01 : "))
    coin = (quartar*0.25) + (dimes*0.10) + (nickles*0.05) + (pennies*0.01)
    formatted_coin = "{:.2f}".format(coin)
    return formatted_coin



while run == True:
    choice = input("Enter What you want: ").lower()
    if choice == "report":
        #print(resources)
        print(f"water : {resources['water']}")
        print(f"coffee : {resources['coffee']}")
        print(f"milk : {resources['milk']}")
    else:
        option = coffee_making(user_choice=choice,will_run=run)
        if option == True: 
            bill = money_calculation()
            print(f"You pay {bill}$")
            if float(bill) >= menu[choice]["cost"]:
                change = float(bill) - menu[choice]["cost"]
                change = "{:.2f}".format(change)
                print(f"Here is your {choice}")
                print(f"Your change is {change}$.")
                resources["water"] = resources["water"] - menu[choice]["ingrediants"]["water"]
                resources["coffee"] = resources["coffee"] - menu[choice]["ingrediants"]["coffee"]
                if menu[choice] == menu["espresso"]:
                    resources['milk'] = resources["milk"]
                else:
                    resources["milk"] = resources["milk"] - menu[choice]["ingrediants"]["milk"]
            else:
                print("You have entered insufficiesnt balance...Try again")
                run = False
        else:
            run = False
            
        

