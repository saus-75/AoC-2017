import sys

with open('in4.txt') as file:
    data = file.readlines()
file.close()

pp_list = []

for pp in data:
    pp.strip('\n')
    pp_list.append(pp.split())

dup = 0

unique = {}
for pp in pp_list:
    for word in pp:
        if (word in unique):
            dup += 1
            unique.clear()
            break
        else:
            unique[word] = 1
    unique.clear()

print("Total passphrases:", len(data))
print("Duplicates:", dup)
print("Valid passphrases:", (len(data) - dup))