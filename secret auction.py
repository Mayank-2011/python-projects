logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
import os
print("Welcome to the secret auction program.")

def find_highest_bid(auction_bids):
    highest_bid = 0
    winner = ""
    for bidder in auction:
        bid_amount = auction[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
        
condition = True

while condition:
    auction = {}
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    auction[name] = bid
    ask = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if ask == "yes":
        os.system('CLS')
    elif ask == "no":
        condition = False
find_highest_bid(auction)

    
    
