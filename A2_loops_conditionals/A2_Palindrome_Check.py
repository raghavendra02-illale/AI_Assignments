#enter a whole number
number = int(input("Enter a number: "))

# Save original number for comparison
original = number

# Start reversed number at 0
reverse = 0

# itirate loop until all digits processed
while number > 0:

    # Get last digit
    digit = number % 10

    # Add digit to the reversed number
    reverse = reverse * 10 + digit

    # Remove the last digit
    number = number // 10

# Print the reversed number
print(f"{original} reversed is {reverse}")

# Check whether the original and reversed numbers are the same
if original == reverse:

    # If equal, the number is a palindrome
    print("Result: Palindrome")

else:

    # If not, it is not a palindrome
    print("Result: Not a Palindrome")