def solve(numheads, numlegs):
    rabbits = (numlegs - (2*numheads))/2
    chickens = numheads - rabbits
    print("Rabbits =", int(rabbits),"\nChickens =", int(chickens))


solve(35, 94)