import sys

with open('in1.txt') as file:
    code = file.read()
file.close()

sum = 0
jump = int(len(code)/2)
print("jump factor: " + str(jump))
code = list(code)

for index, item in enumerate(code, start=0):
    print(item + ': ', end='')
    if (index + 1 < len(code)/2):
        if (item == code[index + jump]):
            print(" matched")
            sum += int(item)
        else:
            print("not matched")
            pass
    else:
        pass
        if (item == code[index - jump]):
            print (str(index - jump) + " ", end='')
            print("matched")
            sum += int(item)
        else:
            print ("not matched")
            pass

# if (code[0] == code[len(code) - 1]):
#     # print ("matched")
#     sum += int(code[len(code) -1])
# else:
#     pass
#     # print ("not matched")

print(sum)