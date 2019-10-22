print("Enter a word")
word = input()
print("Choose an option (1 - Under/2 - Over/3 - Both/4 - Grid")
option = int(input())
if  (option == 1):
    print(word)
    print("*" * len(word))
elif (option == 2):
    print("*" * len(word))
    print(word)
elif (option == 3):
    print("*" * len(word))
    print(word)
    print("*" * len(word))

elif (option == 4):
    print("What size would you want your grid to be?")
    grid_size = int(input())
    grid = 0
    while (grid < grid_size):
        grid = grid + 1
        print(("*" * len(word) + " ") * grid_size )
        print((word + "|") * grid_size)
        print(("*" * len(word) + " ") * grid_size)
else:
    print("Invalid option.")