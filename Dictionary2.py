d = {}
d[1] = 1
d['1'] = 2
d[1] = 3
sum = 0
for i in d:
    sum += d[i]
print(sum)