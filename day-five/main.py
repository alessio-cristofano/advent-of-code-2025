import numpy as np
# 
valid_id_ranges = []
items_id = []
switch_mode = 0
with open("input.txt","r") as file:
    for row in file:
        if row == "\n":
            switch_mode = 1
            continue
        row = row.replace("\n","")
        if switch_mode == 0:
            valid_id_ranges.append((int(row.split("-")[0]),int(row.split("-")[1])))
        else:
            items_id.append(int(row))
# 
# Brute force
# valid_id_ranges = sorted(valid_id_ranges,key=lambda x:x[0]) 
# items_id = sorted(items_id)
valid_counter = 0
for id in items_id:
    for _range in valid_id_ranges:
        if id <= _range[1] and id >= _range[0]:
            valid_counter += 1
            break
print(f"Part 1 | The total number of fresh items is {valid_counter}")
# 
# Part two
# 
valid_id_ranges = sorted(valid_id_ranges,key=lambda x:x[0]) 
merged_ranges = []
i = 0
tmp = []
current_range = valid_id_ranges[0]
while i < len(valid_id_ranges)-1:
    next_range = valid_id_ranges[i+1]
    if current_range[1] >= next_range[0]:
        current_range = (current_range[0],max([next_range[1],current_range[1]]))
    else:
        merged_ranges.append(current_range)
        current_range = next_range
    i += 1
merged_ranges.append(current_range)
# 
count = 0
for r in merged_ranges:
    count += len(range(r[0],r[1]+1))
    # 
print(f"Part 2 | The total number of fresh items is {count}")