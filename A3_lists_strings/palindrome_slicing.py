text = input("Enter a string: ")
clean_text = text.replace(" ", "").lower()
print("Palindrome" if clean_text == clean_text[::-1] else "Not a palindrome")