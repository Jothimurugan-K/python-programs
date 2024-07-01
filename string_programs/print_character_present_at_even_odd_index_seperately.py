str = 'jothimurugan'

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
