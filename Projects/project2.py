import random

password = input("Enter your password: ")

if len(password) < 9:
    print("Password too short.")
else:

    for i in range(3):

        position = random.randint(1, len(password))

        letter = input("Enter letter at position " + str(position) + ": ")

        if letter == password[position - 1]:
            print("Correct")
        else:
            print("Security check failed.")
            break
    else:
        # This runs only if all 3 checks were correct
        print("Security check passed.")
