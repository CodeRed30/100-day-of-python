print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? "))
people = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
tip_as_percent = tip / 100
total_incl_tip = bill + (bill * tip_as_percent)
total_pp = total_incl_tip / people

print(f"Each person should pay: ${total_pp}")
