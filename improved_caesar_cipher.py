text = input("Enter your message: ")

while True:
    try:
        shift = int(input("Enter shift (1-25): "))
        if 1 <= shift <= 25:
            break 
        print("Please enter a number strictly between 1 and 25.")
    except ValueError:
        print("Invalid input. Please enter a valid whole number.")
cipher = ""
for char in text:
    # Is it a letter?
    if char.isalpha():
        # Shift its code.
        code = ord(char) + shift
        if char.isupper():
            first = ord('A')
        else:
            first = ord('a')
       
        code -= first
        code %= 26
        cipher += chr(first + code)
    else:
        cipher += char

print(cipher)
    