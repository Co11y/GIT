list = []
with open("file.txt", 'r+') as filee:
    for date in filee:
        list.append(int(date))

print(list)
sum(list)

