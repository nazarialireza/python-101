

word = 'Python'
count = 0
lines = []
found = False
for item in string.splitlines():
    if item.find(word) != -1:
        if item.find('John:') != -1:
            lines.append(item)
            count += 1
            found = True
if found:
    print('Number of reputation: ' + str(count))
    for line in lines:
        print(line)
else:
    print('There are no result!')
