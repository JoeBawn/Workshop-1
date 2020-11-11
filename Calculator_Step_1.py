#Calculator

#Parameter A
#Parameter B

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# Take input from the user
choice = input("Enter choice(1/2/3/4): ")
num_1 = int(input('Enter your first number: '))
num_2 = int(input('Enter your second number: '))

if choice == "1":
    # Addition
    print('{} + {} = '.format(num_1, num_2))
    print(num_1 + num_2)
elif choice == "2":
    # Subtraction
    print('{} - {} = '.format(num_1, num_2))
    print(num_1 - num_2)
elif choice == "3":
    # Multiplication
    print('{} * {} = '.format(num_1, num_2))
    print(num_1 * num_2)
elif choice == "4":
    # Division
    print('{} / {} = '.format(num_1, num_2))
    print(num_1 / num_2)
    # The format() will help out output look descent and formatted.
