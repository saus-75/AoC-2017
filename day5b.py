import sys

with open('in5.txt') as file:
    data = file.readlines()
file.close()

jump_ls = list(map(int, data))

step = 0
curr = 0
prev = 0
while (True):
    try:
        prev = curr
        curr += jump_ls[curr]
        if (jump_ls[prev] < 3):
            jump_ls[prev] += 1
        else:
            jump_ls[prev] -= 1
        step += 1
    except IndexError:
        # print(jump_ls)
        print ("Steps: ", step)
        break