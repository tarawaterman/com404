print("Please enter a whole number.")
number = int(input())
ans = number % 2
if  (ans == 1):
    print("The number ", number, "is an odd number.")
else:
    print("The number ", number, "is an even number.")