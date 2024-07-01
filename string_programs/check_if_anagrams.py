s1 = 'SILENT'
s2 = 'LISTEN'

if sorted(s1) == sorted(s2):
    print(f'{s1} and {s2} are anagrams')
else:
    print(f'{s1} and {s2} are not anagrams')