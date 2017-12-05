import sys

with open('in2.txt') as file:
    sheet = file.readlines()
file.close()

splitted = []

for val in sheet:
    val.strip('\n')
    splitted.append(val.split())

sum = 0

for val in splitted:
    sum += (max(list(map(int,val))) - min(list(map(int,val))))

print(sum)