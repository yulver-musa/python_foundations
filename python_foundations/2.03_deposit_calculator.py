# To calculate the monthly interest

deposit = float(input())
terms = int(input())
percent = float(input())
percent_decimal = percent / 100

interest = deposit * percent_decimal
interest_per_month = interest / 12
total = deposit + terms * interest_per_month
print(f"{total:.2f}")
