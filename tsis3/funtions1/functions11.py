def isPalindrome(str):
    if str == str[::-1]:
        return True
    else:
        return False


str = input()
print(isPalindrome(str))