target_name = "Miro"


guessed_letters = ""


while True:

    guess = input("Guess the name: ")

    if guess == target_name:
        print("Congratulations! You guessed the name correctly.")
        break  


    hint = ""
    for letter in target_name:
        if letter in guessed_letters:
            hint += letter
        else:
            hint += "_"
    print("Incorrect guess. Hint:", hint)


    guessed_letters += guess