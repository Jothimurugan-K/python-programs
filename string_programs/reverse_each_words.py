str = "My name is Aksash"

words = str.split()
print(words)

ans = []

for word in words:
    ans.append(word[::-1])

print(ans)

print(' '.join(ans))