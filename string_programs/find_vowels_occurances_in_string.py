string = 'Heythisisjothimurugan'

d = {}
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

for ch in string:
    if ch in vowels:
        d[ch] = d.get(ch, 0) + 1
print(d)

for k, v in d.items():
    print(f'{k} present {v} times')