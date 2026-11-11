text = input("Enter a string: ")
vowels = "aeiou"
count = sum(1 for character in text.lower() if character in vowels)
print("Number of vowels:", count)