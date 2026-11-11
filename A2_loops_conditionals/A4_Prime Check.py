# Take number from user
number = int(input("Enter a number: "))

# Numbers below 2 are not prime
if number < 2:

    # Print the result
    print(f"{number} is not prime")

else:

    # Start checking from 2
    divisor = 2

    # Keep track if we find a divisor
    found = 0

    # Check all possible divisors
    while divisor < number:

        # Check if number divides evenly
        if number % divisor == 0:

            # Show the divisor
            print(f"{number} is divisible by {divisor}")

            # Mark that we found a divisor
            found = 1

            # Stop the loop
            break

        # Go to the next number
        divisor = divisor + 1

    # If no divisor was found
    if found == 0:

        # Number is prime
        print(f"{number} is prime")

    else:

        # Number is not prime
        print(f"{number} is not prime")