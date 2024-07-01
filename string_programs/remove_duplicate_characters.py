s = 'AAABBCC'

# Method 1
d = ''
for x in s:
    if x not in d:
        d = d + x
print(d)

# Method 2
d = []

for x in s:
    if x not in d:
        d.append(x)
print(''.join(d))

# Method 3

d = set(s)
print(''.join(d))

