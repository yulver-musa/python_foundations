length_cm = int(input())
width_cm = int(input())
height_cm = int(input())
percentage = float(input())

tanks_volume = length_cm * width_cm * height_cm
tanks_litres = tanks_volume * 0.001
percentage_decimal = percentage / 100
available = tanks_litres - (tanks_litres * percentage_decimal)

print(available)
