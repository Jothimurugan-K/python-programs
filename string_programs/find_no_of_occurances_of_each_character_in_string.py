s = 'AABBBCDDDD'

l = []

for ch in s:
    if ch not in l:
        l.append(ch)

print(l)

for ch in l:
    print(f'{ch} present {s.count(ch)} times')