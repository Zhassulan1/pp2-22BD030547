import random
r = random.randint(1, 20)

print("Hello! What is your name?")
name = input()

print(f"Well, {name}, I am thinking of a number between 1 and 20.")
print("Take a guess.")
guess = int(input())
count = 1

running = True
while running:
    if guess == r:
        print(f"Good job, {name}! You guessed my number in {count} guesses!")
        running = False
        continue
    elif guess < r:
        print("Your guess is too low.")
        print("Take a guess.")
        count += 1
    else:
        print("Your guess is too high.")
        print("Take a guess.")
        count += 1
    guess = int(input())

