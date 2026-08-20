print("=== Welcome to the anagram python program ===".upper())
text_1 = input("Enter the first text : ").lower()
text_2 = input("Enter the second text : ").lower()
x  = text_1.replace(" ","")
y  = text_2.replace(" ","")
if x == "" and y == "":
    print("The both text are not Anagram.")
elif sorted(x) == sorted(y):
    print("The both text are Anagram.")
else:
    print("The both text are not Anagram.")