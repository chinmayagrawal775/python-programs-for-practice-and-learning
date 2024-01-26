import json

f = open("file2.txt", "r")
content = f.read()
splitcontent = content.splitlines()
# print(splitcontent)

# seven1 = splitcontent[0:7]
# seven2 = splitcontent[7:14]
# print(seven1)
# print(seven2)

i = 0
s = 0
e = 7
data = []
while(i < 138):
    data.append(splitcontent[s:e])
    data[i].pop(1)
    data[i].pop(2)
    data[i].pop(3)
    data[i].pop(3)
    s = s + 7
    e = e + 7
    i = i + 1

ed = ['139', '3:13', 'Advance JavaScript Completed Now What Next']
data.append(ed)
# print(*data, sep="\n")

for d in data:
    print(d[0] + "," + d[1] +  "," + d[2])

# with open('readme.txt', 'w') as f:
#     f.writelines(splitcontent)

# with open('readme.txt', 'w') as f:
#     for content in splitcontent:
#         f.write(content)
#         f.write('\n')

# with open('readme.txt', 'w') as f:
#     f.writelines(data)