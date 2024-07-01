str = 'One Two Three Four Five Six'

words = str.split()

count = 0
words_reversed = []

for word in words:
    if count%2 == 0:
        words_reversed.append(word)
        count = count + 1
    else:
        words_reversed.append(word[::-1])
        count = count + 1

print(words_reversed)
print(' '.join(words_reversed))
