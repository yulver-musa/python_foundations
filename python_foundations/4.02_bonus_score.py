# A whole number (initial points) is given.
# Bonus points are added to it according to the following rules:
#
# Main bonus:
#  - If the number is up to 100 (inclusive),
#  the bonus is 5 points.
#  - If the number is greater than 100,
#  the bonus is 20% of the number.
#  - If the number is greater than 1000,
#  the bonus is 10% of the number.
#
# Additional bonus (applied on top of the main bonus):
#  - If the number is even → +1 point.
#  - If the number ends with 5 → +2 points.
#
# Write a program that calculates:
#  1) The total bonus points received.
#  2) The total points (initial number + bonus).

number = int(input())
bonus = 0

if number <= 100:
    bonus = 5
elif 100 < number <= 1000:
    bonus = number * 0.2
elif number > 1000:
    bonus = number * 0.1

if number % 2 == 0:
    bonus = bonus + 1
elif number % 10 == 5:
    bonus = bonus + 2

print(bonus)
print(bonus + number)
