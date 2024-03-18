# Day 9 Project:👌

from replit import clear
# HINT: You can call clear() to clear the output in the console.


from art import auction_logo


def win_bidder(bidders_info):
    print("The Aution is completed successfully")
    max_bid = 0
    bid_name = ''
    for bid in bidders_info:
        if bidders_info[bid] > max_bid:
            max_bid = bidders_info[bid]
            bid_name = bid
    print(f"The winner is {bid_name} with a bid of ${max_bid}.")


print(auction_logo)
print("Welcome to the secret auction program.")
other_bidders = 'yes'
bidders_dict = {}
while other_bidders == 'yes':
    bidder_name = input("What is your name?: ")
    bid_value = int(input("What's your bid?: $"))
    bidders_dict[bidder_name] = bid_value
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    clear()
win_bidder(bidders_info=bidders_dict)
