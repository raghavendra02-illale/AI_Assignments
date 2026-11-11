#enter a whole number
number = int(input("Enter a number: "))

#Save original number BCZ 'number' will change inside the loop
original = number

#Start reversed number at 0
reverse = 0

#itirate while loop there are still digits left
while number > 0:

    # Get last digit of number
    digit = number % 10

    # Add last digit to reversed number
    reverse = reverse * 10 + digit

    # Remove last digit from the number
    number = number // 10

# Display the original number and its reversed value
print(f"Reverse of {original} is {reverse}")