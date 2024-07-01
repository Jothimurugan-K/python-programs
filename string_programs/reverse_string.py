str = "Program"

# Method 1
print(str[::-1])

# Methd 2

str1 = ''
for letter in str:
    str1 = letter + str1
print(str1)