# Even or odd
# Problem
''' Check wheather number is even or odd '''

# Solution

print("*** Welcome to Even or odd checker *** \n")
#Asking user to input the number to be checked
num = float(input("Which natural number do you want to check?\n Number: "))
number = int(round(num))

result = number % 2
print()

#printing the result
if result == 0:
    print(f"Answer: '{number}' is an even number.")
else:
    print(f"Answer: '{number}' is an odd number.")

print()
print("*** Thank You ***")
