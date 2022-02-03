def check_palindrome(s):
    if(s[:]==s[::-1]):
        return True
    else:
        return False

mystr = input("Enter a string: ")
print(check_palindrome(mystr))