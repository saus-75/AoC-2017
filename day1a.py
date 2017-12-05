import sys

with open('in1.txt') as file:
    code = file.read()
file.close()

sum = 0
code = list(code)

for index, item in enumerate(code, start=0):
    print(item + ': ', end='')
    if (index + 1 < len(code)):
        if (item == code[index + 1]):
            print("matched")
            sum += int(item)
        else:
            print("not matched")

if (code[0] == code[len(code) - 1]):
    print ("matched")
    sum += int(code[len(code) -1])
else:
    print ("not matched")

print(sum)