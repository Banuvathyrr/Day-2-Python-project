print("Welcome to the tip calculator!")
bill_amount=input("What was the total bill?")
new_bill_amount=float(bill_amount[1:])
tip_amount=int(input("How much tip would you like to give? 10, 12, or 15?"))
split_number= int(input("How many people to split the bill?"))
tip_amount_as_percent=tip_amount/100
total_tip_amount=new_bill_amount*tip_amount_as_percent
total_bill_shared= (new_bill_amount+total_tip_amount)/split_number
amount_to_be_paid_each=round(total_bill_shared,2)
print(f"Each person should pay ${amount_to_be_paid_each}")