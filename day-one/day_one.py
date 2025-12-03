import math
start = 50
base = 100
count = 0
# 
steps = []
with open("input.txt","r") as file:
    for row in file:
        if row[0] == "L":
            steps.append(-int(row.strip()[1:]))
        else:
            steps.append(int(row.strip()[1:]))
#
status = start
for s in steps:
    old_status = status
    status = status + s
    if (status) <= 0:
        count = count + math.floor((-status)/base)
        if old_status != 0:
            count = count+1
    elif (status) >= 100:
        count = count + math.floor(status/base)
    status = status%base
print(count)