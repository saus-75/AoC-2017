import sys

with open('in5.txt') as file:
    data = file.readlines()
file.close()

jump_ls = list(map(int, data))

# print(jump_ls)

step = 0
curr = 0
prev = 0
while (True):
    try:
        prev = curr
        curr += jump_ls[curr]
        jump_ls[prev] += 1
        step += 1
    except IndexError:
        print (step)
        break