import random
print("Number guessing game")

number = random.randint(1,9)

chances = 0

print("Gues a number between 1 and 9")

while chances < 5:
    guess = int(input("Enter your guess:-"))

    if guess == number:
        print("Congragulations you won")
        break

    elif guess < number:
        print("your guess was to low:Guess a nubmer higher than",guess)

    else:
        print("Your guess was to high: Guess a number lower than",guess)

    chances +=1
    
if not chances < 5:
    print("You Lose the number was",number)