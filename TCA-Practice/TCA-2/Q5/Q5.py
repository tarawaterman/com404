health = 100
number = 0
print("Your health is", health, "%. Escape is in progress...")

while (number < 5):
    print("...Oh dear, who is that?")
    response_1 = input()
    if  (response_1 == "Smiler's Bot"):
        health = health - 20
        print("Time to jam out of here!")
        number = number + 1
    elif (response_1 == "Hacker"):
        health = health + 20
        print("Yay! Better follow this one!")
        number = number + 1
    else:
        print("Phew, just another emoji!")
        number = number + 1

print("Escaped! Health is", health, "%")