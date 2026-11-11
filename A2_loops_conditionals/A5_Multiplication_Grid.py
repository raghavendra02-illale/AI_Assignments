# Go through rows 1 to 5
for row in range(1, 6):

    # Start with an empty line
    line = ""

    # Go through columns 1 to 5
    for column in range(1, 6):

        # Multiply row and column
        value = row * column

        # Add the answer to the line
        line = line + f"{value:5}"

    # Print the row
    print(line)