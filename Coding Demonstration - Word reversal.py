string = 'university'
rev = ''
#iterate over a sequence, counting backwords
for j in range (len(string) - 1, -1, -1):
#concatenate character at index j
    rev += string[j]

print(rev)