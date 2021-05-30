def snake_case(word):
    rev = ''.join(reversed(word))
    if (word == rev):
        return True
    return False

word = "kajxak"
palindrome = snake_case(word)
if (palindrome):
    print("Yes")
else:
    print("No")
