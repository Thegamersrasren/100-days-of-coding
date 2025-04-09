import os

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def div(n1, n2):
    if n2 == 0:  # Prevent division by zero
        return "Error: Division by zero is not allowed."
    return n1 / n2

def mult(n1, n2):
    return n1 * n2

calculator = {
    "+": add,
    "-": sub,
    "/": div,
    "*": mult
}

def calc():
    done = False
    while not done:
        n1 = float(input("What is the first number? "))

        for symbol in calculator:
            print(symbol)

        equation = input("What would you like to do? ")
        if equation not in calculator:
            print("Invalid operation. Please choose a valid symbol.")
            continue

        n2 = float(input("What is the second number? "))
        answer = calculator[equation](n1, n2)
        print(f"{n1} {equation} {n2} = {answer}")

        choice = input("Do you wish to continue calculating with this result? (Y or N): ").lower()

        if choice == "n":
            done = True
            print("Goodbye")
            os.system('cls')  # This clears the console in Windows
        elif choice == "y":
            n1 = answer
        else:
            print("Invalid choice. Exiting the calculator.")
            done = True
calc()