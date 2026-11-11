# Take the first number
number = int(input("Enter number 1: "))

# At first, this is the largest
largest = number

# At first, keep the same number here
second_largest = number

# Take the second number
number = int(input("Enter number 2: "))

# Check if it is bigger than largest
if number > largest:

    # Old largest becomes second largest
    second_largest = largest

    # New number becomes largest
    largest = number

# Check if it can be second largest
elif number > second_largest and number != largest:

    # Change second largest
    second_largest = number

# Take the third number
number = int(input("Enter number 3: "))

# Check if it is the biggest
if number > largest:

    # Move old largest to second place
    second_largest = largest

    # Make this the largest
    largest = number

# Check if it is second largest
elif number > second_largest and number != largest:

    # Change second largest
    second_largest = number

# Take the fourth number
number = int(input("Enter number 4: "))

# Check if it is the biggest
if number > largest:

    # Move old largest down
    second_largest = largest

    # Change largest
    largest = number

# Check if it is second largest
elif number > second_largest and number != largest:

    # Change second largest
    second_largest = number

# Take the fifth number
number = int(input("Enter number 5: "))

# Check if it is the biggest
if number > largest:

    # Move old largest to second place
    second_largest = largest

    # Change largest
    largest = number

# Check if it is second largest
elif number > second_largest and number != largest:

    # Change second largest
    second_largest = number

# Print the answers
print(f"Largest : {largest}")
print(f"Second largest: {second_largest}")