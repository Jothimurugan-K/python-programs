str = 'jothimurugan'

# Method 2
count = 0
print("Odd index characters...")
for x in str:
    if count%2==0:
        print(x)
    count = count + 1

print("even index characters...")
for x in str:
    if count%2 != 0:
        print(x)
    count = count + 1

# Method 2
odd_char = str[0::2]
even_char = str[1::2]

print(odd_char)
print(even_char)