print("Welcome to the tip calculator!")

bill_amount = float(input("What was your total bill? $"))
tip = float(input("How much tip would you like to give? 10,12 or 15?"))
person = float(input("How many people to split the bill?"))
count = ((bill_amount + ((bill_amount *tip)/100)/person)
rounded_bill = round(count,2)
print(f"Each person should pay: $ {rounded_bill}")