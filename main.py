MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}



money = 0

def coffee_feasible(coffee):
        data = MENU[coffee]['ingredients']
        doable = True
        for i in data:
            if resources[i] < data[i]:
                doable=False
                print(f"Not enough {i}.")
        return doable

def coffee_maker(coffee):
    data = MENU[coffee]['ingredients']
    for i in data:
        resources[i] -= data[i]


def price_return(coffee):
    return MENU[coffee]['cost']

def insert_coins(price):
    global money
    print("Please insert coins.")
    quarters = int(input("How many quarters? :"))
    dimes = int(input("How many dimes? : "))
    nickles = int(input("How many nickles? : "))
    pennies = int(input("How many pennies? : "))
    total = (quarters*0.25) + (dimes*0.1) + (nickles*0.05) + (pennies*0.01)
    if total>=price:
        print("Here is your coffee.")
        money+=price
        if total>price:
            print(f"Here is {round(total-price,2)} in change.")
        return True
    elif total<price:
        print("Not enough money.Money refunded")
        return False


def machine():
    is_making=True
    while is_making:
        function = input("What would you like? (espresso/latte/cappuccino): ")
        if function == 'report':
            print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: ${money}")
        else:
            is_okay=coffee_feasible(function)
            if is_okay:
                price=price_return(function)
                is_feasible=insert_coins(price)
                if is_feasible:
                    coffee_maker(function)

machine()
