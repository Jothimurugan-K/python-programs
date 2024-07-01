str = "I am writing python programs"

words = str.split(" ")
print(words[::-1])

# Method 1
reverse_words = ''
for word in words:
    reverse_words =  word + ' ' + reverse_words

print(reverse_words)

# Method 2
print(' '.join(words[::-1]))
