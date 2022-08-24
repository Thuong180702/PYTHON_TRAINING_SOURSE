age = int(input("What is your current age?: "))

Year_remaining = 100 - age
Days_remaining = Year_remaining * 365
Weeks_remaining = Year_remaining * 52
Months_remaining = Year_remaining * 12

print(f"You have {Days_remaining} days, {Weeks_remaining} weeks, {Months_remaining} months, {Year_remaining} years.")
