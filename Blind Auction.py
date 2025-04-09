import os



bid = {}

def highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for name, bid_amount in bidding_dictionary.items():
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = name
    print(f"The winner is {winner}, they bid ${highest_bid}")

more = False
while not more:
    print("Welcome to the Blind Auction")
    nAME = input("What is thy name: ")
    try:
        bid_amount = int(input("How much do you bid: $"))  # Convert to integer for proper comparison
    except ValueError:
        print("Sorry that is not a biddable value type in a number")

    
    bid[nAME] = bid_amount

    players = input("Are there more players? Yes or no: ").lower()
    if players == "no":
        more = True
    else:
        os.system('cls')



highest_bidder(bid)