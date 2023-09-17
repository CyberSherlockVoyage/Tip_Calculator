print("Welcome to the tip calculator!")

bill =float(input("What was the total bill? $ "))
tip = int(input("How much tip would you like to give? 10, 12 or 15?  "))
person = int(input("How many people to spilt the bill? "))

Tip_Conversion = tip / 100
Total_tip = bill * Tip_Conversion
Total_bill = bill + Total_tip
bill_per_person = Total_bill / person
Amount = round(bill_per_person,2)

print(f"Each person should pay: ${Amount}")
