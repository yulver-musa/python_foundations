# Ani from class 10B needs pens, markers, and board cleaner.
# Prices: pens=5.80, markers=7.20, cleaner=1.20 per liter.
# Input: packs of pens, packs of markers, liters cleaner, discount%.
# Output: total amount after discount.
pkts_of_pens = int(input())
pkts_of_markers = int(input())
ltrs_of_cleaner = int(input())
discount_rate = int(input())

price_of_pens = 5.8
price_of_markers = 7.2
price_of_cleaner = 1.2
discount_percentage = discount_rate / 100

total_pens = pkts_of_pens * price_of_pens
total_markers = pkts_of_markers * price_of_markers
total_cleaner = ltrs_of_cleaner * price_of_cleaner

sub_sum = total_pens + total_markers + total_cleaner

total_sum = sub_sum - (sub_sum * discount_percentage)

print(total_sum)
