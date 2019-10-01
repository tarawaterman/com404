print("Please enter the first whole number.")
first_number = int(input())

print("Please enter the second whole number.")
second_number = int(input())

print("Please enter the third whole number.")
third_number = int(input())

ans_one = first_number % 2
ans_two = second_number % 2
ans_three = third_number % 2

if  (ans_one + ans_two + ans_three == 1):
    print("There were 2 even numbers and 1 odd number.")
elif (ans_one + ans_two + ans_three == 2):
    print("There was 1 even number and 2 odd numbers.")
elif (ans_one + ans_two + ans_three == 3):
    print("All 3 numbers were odd numbers")
elif (ans_one + ans_two + ans_three == 0):
    print("All 3 numbers were even numbers")