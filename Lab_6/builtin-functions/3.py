str = input("Write your string: ")

if str == "".join(reversed(str)):
    print("This string is Palindrome")
else:
    print("This is NOT Palindrome")    