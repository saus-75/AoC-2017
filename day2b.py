import sys

with open('in2.txt') as file:
    sheet = file.readlines()
file.close()

sum = 0

splitted = []

for val in sheet:
    val.strip('\n')
    splitted.append(val.split())

for val in splitted:
    ls = list(map(int,val))
    ls.sort(reverse=True)
    for index, x in enumerate(ls, start=0):
        for y in range(index+1, len(ls)):
            if (x % ls[y] == 0):
                print(str(x) + " " + str(ls[y]))
                sum += (x/ls[y])
                break

print(sum)
