sq_m = float(input())

price_sq_m = 7.61

discount = 0.82

total_price = sq_m * price_sq_m
total_price_discount = total_price * discount

discount_price = total_price - total_price_discount

print(f'The final price is: {total_price_discount:.2f} lv.')
print(f'The discount is: {discount_price:.2f} lv.')
