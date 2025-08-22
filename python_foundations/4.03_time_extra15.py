# Time + 15 Minutes
# Write a program that:
#  - Reads hours and minutes from a 24-hour day, entered by the user.
#  - Calculates what the time will be after 15 minutes.
#  - Prints the result in the format hours:minutes.
#
# Rules:
#  - Hours are always between 0 and 23.
#  - Minutes are always between 0 and 59.
#  - Hours can be printed with one or two digits (e.g., 0, 5, 12, 23).
#  - Minutes must always be printed with two digits (e.g., 05, 09, 30).

hours = int(input())
minutes = int(input())

extra_minutes = 15

hours_in_minutes = hours * 60

total_minutes = hours_in_minutes + minutes + extra_minutes

final_hours = total_minutes // 60
if final_hours >= 24:
    final_hours = final_hours - 24
final_minutes = total_minutes % 60

if final_minutes < 10:
    print(f'{final_hours}:0{final_minutes}')
else:
    print(f'{final_hours}:{final_minutes}')
