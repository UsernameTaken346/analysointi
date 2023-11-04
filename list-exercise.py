furniture_list = ["table", "chair", "shelf", "sofa", "bed"]

print("Whole list:", furniture_list)

print("First two elements:", furniture_list[:2])

for item in furniture_list:
    if item == "sofa":
        print("Sofa is in the list.")
        break

# harjoitus 2

from random import randint

thrownDiceNumbers = []

for _ in range(5):
    thrownDiceNumbers.append(randint(1, 6))

print("Whole list:", thrownDiceNumbers)

list_sum = sum(thrownDiceNumbers)
print("Sum of list values:", list_sum)

highest_value = max(thrownDiceNumbers)
print("Highest value in the list:", highest_value)