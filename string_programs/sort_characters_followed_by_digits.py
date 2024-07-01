input = 'B4A1D3'

alp = []
digits = []

for x in input:
    if x.isalpha():
        alp.append(x)
    else:
        digits.append(x)

output = (sorted(alp) + sorted(digits))
print(''.join(output))