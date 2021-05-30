def Palindrome(s):
    rev = ''.join(reversed(s))
    if (s == rev):
        return True
    return False

s = "kajxak"
ans = Palindrome(s)
if (ans):
    print("Yes")
else:
    print("No")