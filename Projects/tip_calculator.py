# Day 2 Project👌

print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
split_number = int(input("How many people to split the bill? "))
# pay_amount = (total_bill/split_number)*tip_percent
pay_amount = (total_bill/split_number)*(1+tip_percent/100)
print(f"Each person should pay: ${round(pay_amount,2)}")
# Formula: (total_bill+total_bill*tip_percent/100)/split_number
# therefore total_bill/split_number*(1+tip_percent/100)

