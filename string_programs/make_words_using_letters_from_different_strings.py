s1 = 'abcdefg'
s2 = 'xyz'
s3 = '12345'

i= j= k = 0


for ch in range(max(len(s1), len(s2), len(s3))):
    output = ''
    if i<len(s1):
        output = output+s1[i]
        i = i+1
    if j<len(s2):
        output = output+s2[j]
        j = j+1
    if k<len(s3):
        output = output+s3[k]
        k=k+1
    print(output)
