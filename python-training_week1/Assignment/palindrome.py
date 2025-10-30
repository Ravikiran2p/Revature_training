text=input("Enter a word or number:")
reversed_text=text[::-1]
if text==reversed_text:
    print("word is palindrome")
else:
    print("word is not palindrome")