print("==== welcome to the Palindrome program ====".title())
text = input("Enter the text:").lower()
text = text.replace(" ", "")
reversed_text = text[::-1]
if text == "":
    print("The string is not a palindrome.".title())
elif text == reversed_text:
    print("This is a palindrome.".title())
else:
    print("This is not a palindrome".title())