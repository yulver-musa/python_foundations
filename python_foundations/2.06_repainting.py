cover = int(input())
paint = int(input())
diluter = int(input())
labour_hours = int(input())

extra_paint = paint * 0.1
extra_cover = 2
bags = 0.4

cover_price = 1.5
paint_price = 14.5
diluter_price = 5

cover_total_price = (cover + extra_cover) * cover_price
paint_total_price = (paint + extra_paint) * paint_price
diluter_total_price = diluter * diluter_price

material_total = cover_total_price + paint_total_price + diluter_total_price + bags

labour_price = material_total * 0.3

labour_total_price = labour_price * labour_hours

total_cost = material_total + labour_total_price

print(f'{total_cost:.2f}')
