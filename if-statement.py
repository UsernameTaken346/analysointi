number1 = 8
number2 = 7
number3 = 3


if number1 == number2 == number3:
    print("All numbers are equal")


if (number1 == number2) or (number2 == number3):
    print("number1 and number2 are equal, or number2 and number3 are equal")


if number1 > number2 and number1 > number3:
    print("number1 is greater than number2 and number3")


if number1 > number2:
    print("number1 is greater than number2")
elif number2 > number3:
    print("number2 is greater than number3")

if number1 == number2:
    print("number1 and number2 are equal")
elif number1 == number3:
    print("number1 and number3 are equal")

name1 = "Alice"
name2 = "Bob"
name3 = "Alice"

if name1 == name2:
    print("name1 and name2 are equal")


if name1 != name2:
    print("name1 and name2 are not equal")


if name1 == name2:
    print("name1 and name2 are equal")
elif name1 == name3:
    print("name1 and name3 are equal")
