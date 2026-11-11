# Take number from user
number = int(input("Enter a number: "))

# Start all counters from 0
even = 0
odd = 0
zero = 0

# Keep checking the digits
while number > 0:

    # Get the last digit
    digit = number % 10

    # Remove the last digit
    number = number // 10

    # Check if digit is zero
    if digit == 0:

        # Add 1 to zero count
        zero = zero + 1

    # Check if digit is even
    elif digit % 2 == 0:

        # Add 1 to even count
        even = even + 1

    else:

        # Add 1 to odd count
        odd = odd + 1

# Print the counts
print(f"Even digits : {even}")
print(f"Odd digits : {odd}")
print(f"Zero digits : {zero}")