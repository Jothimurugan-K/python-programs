str1 ="jothi"
str2 ="murugan"

i = 0
j = 0
str = ''

max_len = max(len(str1), len(str2))

for d in range(max_len):
    if d<len(str1):
        str = str + str1[d]
    if d<len(str2):
        str = str + str2[d]

print(str)

# Method 2
# while i <len(str1) or j <len(str2):
#     if i < len(str1):
#         str = str + str1[i]
#         i = i+1
#     if j < len(str2):
#         str = str + str2[j]
#         j = j+1
#
# print(str)