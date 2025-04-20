Starbucks = [
    {"Flavours": "Espresso", "Water": 50, "Coffee": 50, "Milk": 0, "Price": 1.50},
    {"Flavours": "Latte", "Water": 200, "Coffee": 24, "Milk": 150, "Price": 2.50},
    {"Flavours": "Cappuccino", "Water": 250, "Coffee": 24, "Milk": 100, "Price": 3.00}
]
resources = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
}
Money = 0
Penny = 0.01
Nickel = 0.05
Dime = 0.10
Quater = 0.25

def enough(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print("Sorry there is not enough", item)
            return False
    return True

while True:
    order = input("What would you like to order (Espresso/Latte/Cappuccino) or 'Off' to turn off the machine or 'Report' to see what's left: ").lower()
    if order == "off":
        break
    elif order == "report":
        print(f"Water: {resources['Water']}ml")
        print(f"Milk: {resources['Milk']}ml")
        print(f"Coffee: {resources['Coffee']}g")
        print(f"Money: ${Money:.2f}")
    elif order in ["espresso", "latte", "cappuccino"]:
        # Get the drink index
        drink_index = 0 if order == "espresso" else 1 if order == "latte" else 2
        drink = Starbucks[drink_index]
        
        print(f"{drink['Flavours']} costs ${drink['Price']:.2f}")
        nump = float(input("How Many pennies do you wish to input "))
        numn = float(input("How Many Nickels do you wish to input "))
        numd = float(input("How Many Dimes do you wish to input "))
        numq = float(input("How Many Quaters do you wish to input "))
        added = (nump * Penny) + (numn * Nickel) + (numd * Dime) + (numq * Quater)
        
        if enough({"Water": drink["Water"], "Milk": drink["Milk"], "Coffee": drink["Coffee"]}):
            if added >= drink['Price']:
                Money += added
                resources["Water"] -= drink["Water"]
                resources["Coffee"] -= drink["Coffee"]
                if drink["Milk"] > 0:
                    resources["Milk"] -= drink["Milk"]
        
                if added > drink['Price']:
                    change = added - drink['Price']
                    print(f"Here is your change: ${change:.2f}")
                print("Enjoy your coffee!")
            else:
                print("Sorry, that's not enough money. Money refunded.")
        else:
            print("Transaction canceled due to insufficient resources.")
    else:
        print("Invalid input. Please try again.")