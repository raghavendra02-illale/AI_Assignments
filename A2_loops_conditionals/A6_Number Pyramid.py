# Ask how many rows we need
rows = int(input("Enter rows: "))

# Go through each row
for i in range(1, rows + 1):

    # Find how many spaces we need
    spaces = rows - i

    # Print the spaces
    for j in range(spaces):

        # Stay on the same line
        print(" ", end="")

    # Print numbers for this row
    for j in range(1, i + 1):

        # Print number with a space
        print(j, end=" ")

    # Move to the next line
    print()