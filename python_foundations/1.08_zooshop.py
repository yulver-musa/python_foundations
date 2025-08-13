dog_food_pkts = int(input())
cat_food_pkts = int(input())

price_per_dog_food = 2.5
price_per_cat_food = 4

total_dog_food_price = dog_food_pkts * price_per_dog_food
total_cat_food_price = cat_food_pkts * price_per_cat_food

total_sum = total_dog_food_price + total_cat_food_price

print(f'{total_sum} lv.')
