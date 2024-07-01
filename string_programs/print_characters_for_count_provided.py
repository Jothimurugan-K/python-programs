input = 'a4b3c2'

output = ''

for ch in input:
    if ch.isalpha():
        x = ch
    else:
        d = int(ch)
        output = output + d*x
print(output)