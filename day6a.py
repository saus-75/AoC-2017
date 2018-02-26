import sys

with open('in6.txt') as file:
    data = file.readlines()
file.close()

blocks = list(map(int,data[0].strip().split('\t')))

b_bank = {}

copy = blocks

while(str(copy) not in b_bank.keys()):
    value = max(copy)
    index = copy.index(max(copy))
    copy[index] = 0
    

# print(blocks.index(max(blocks)))

