# Basketball equipment:
# Input: yearly training fee.
# Costs: shoes=60% of fee, outfit=80% of shoes, ball=25% of outfit, accessories=20% of ball.
# Output: total expenses.

yearly_cost = int(input())

shoes_cost = yearly_cost - (yearly_cost * 0.4)
suit_cost = shoes_cost - (shoes_cost * 0.2)
ball_cost = suit_cost * 0.25
accessories_cost = ball_cost * 0.2

total_cost = yearly_cost + shoes_cost + suit_cost + ball_cost + accessories_cost

print(f'{total_cost:.2f}')
