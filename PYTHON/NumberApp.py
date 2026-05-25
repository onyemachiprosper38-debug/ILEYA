import random

Random = 56
for random_number in range(1,5):

    guess = int(input("Guess number "))
    
    
    if (guess > Random):
        print("Number is lower")
    
    elif (guess < Random):
        print("Number is higher")

    if (guess == Random):
        print("Number is correct ")
        break

    elif(guess > 100):
        print("warning number is not accepted")

    print(random.randrange (1, 100))

    while True:
        correct_guess = 5

    if (correct_guess == 1):
        print("Lengendary ")

    elif (correct_guess == 2):
        print("Excellent ")

    elif (correct_guess == 3 or 4):
        print("Good ")

    else:
        print("No win Better luck")

print("The coerrect guessing number 56 ")
