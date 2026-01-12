# Ask the user to enter a number
number = input("Enter a number: ")

# Convert to integer
number = int(number)

# Print the number
print("The number entered was", number)

# Even or odd check
if (number % 2) == 0:
    print("That is an even number")
else:
    print("That is an odd number")

# Divisible by 10 check
if (number % 10) == 0:
    print("The number is divisible by 10")
else:
    print("The number is not divisible by 10")
