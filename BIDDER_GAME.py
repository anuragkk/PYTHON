bidders = {}
print("Welcome to online bidding ")


def take_bid():
    name = input("Please enter your name \n")
    bid = input("what is your bidding amount is $\n")
    bidders[name] = bid


def find_highest_bid():
    highest_bid = 0
    winner = ""
    for name in bidders:
        bidding_value = int(bidders[name])
        if bidding_value >= highest_bid:
            highest_bid = bidding_value
            winner = name

    print(f"The winner is {winner} with the highest bid of {highest_bid}$")


while True:
    take_bid()
    option = input("does anyone else want to make the bid??\n").lower()
    if option != "y":
        find_highest_bid()
        break
