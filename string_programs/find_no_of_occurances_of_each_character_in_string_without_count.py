s = 'AABCC'

l = {}

for ch in s:
    l[ch] = l.get(ch, 0) + 1

print(l.values())