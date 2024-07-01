s = 'level'

reverse = ''
for ch in s:
    reverse = ch + reverse
if s == reverse:
    print("Yes this is palindrome")
else:
    print("No this is not palindrome")