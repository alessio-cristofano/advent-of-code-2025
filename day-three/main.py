from typing import List
import numpy as np


def find_max_battery(pack:List[int],length:int):
    if len(pack) == length:
        return pack
    length -= 1
    
    if length == -1:
        return []
    
    left_split: List[int] = pack[0:-length] or pack
    left_digit: int = max(left_split)
    idx: int = pack.index(left_digit)
    right_split: List[int] = pack[idx+1:] 
    left_list: List[int] = [left_digit]

    left_list.extend(find_max_battery(right_split,length))
    return left_list

# read input
packs = []
with open("input.txt","r") as file:
    for row in file:
        row = row.replace("\n","")
        pack = [int(d) for d in row]
        packs.append(pack)

# compute joltage

joltage_part1 = 0
joltage_part2 = 0
n_part1 = 2
n_part2 = 12
for pack in packs:
    joltage_list_part1 = find_max_battery(pack,2)
    for i,jol in enumerate(joltage_list_part1[::-1]):
        joltage_part1 += jol*10**i

    joltage_list_part2 = find_max_battery(pack,12)
    for i,jol in enumerate(joltage_list_part2[::-1]):
        joltage_part2 += jol*10**i

print(f'Part one answer: {joltage_part1}')
print(f'Part two answer: {joltage_part2}')
