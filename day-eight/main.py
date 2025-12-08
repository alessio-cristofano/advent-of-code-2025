import numpy as np
from typing import List,Set
# 
def distance(x,y):
    return np.sqrt(np.sum(np.square(x-y)))    

coordinates = []
with open("input.txt","r") as file:
    for row in file:
        row = row.replace("\n","")
        coordinates.append(np.array([int(r) for r in row.split(",")]))
# 
# Compute all the distances
# 
distances = []
for i,node in enumerate(coordinates):
    for j in range(i+1,len(coordinates)):
        distances.append((i,j,distance(node,coordinates[j])))
#
distances = sorted(distances,key=lambda d:d[2])
spare_points = range(len(coordinates))
boxes = []

# Part 1
connections = 0
while connections < 1000:
    link = distances.pop(0)
    boxes_flat = [bs for b in boxes for bs in b]
    
    if link[0] in boxes_flat and link[1] in boxes_flat:
        for b in boxes: 
            if link[0] in b:
                b0 = b
            if link[1] in b:
                b1 = b
        if b1 != b0:
            
            b0.extend(b1)
            boxes.pop(boxes.index(b1))
        
    elif link[0] in boxes_flat:
        for b in boxes: 
            if link[0] in b:
                b.append(link[1])
    
    elif link[1] in boxes_flat:
        for b in boxes: 
            if link[1] in b:
                b.append(link[0])
    # 
    else:
        new_box = [link[0],link[1]]
        boxes.append(new_box)

    connections += 1
# 
boxes_length = sorted([len(b) for b in boxes],reverse=True)
print(boxes_length[:3])
print(np.prod(boxes_length[:3]))
# 
# Part 2
# 
# Compute all the distances
# 
distances = []
for i,node in enumerate(coordinates):
    for j in range(i+1,len(coordinates)):
        distances.append((i,j,distance(node,coordinates[j])))
#
distances_sorted = sorted(distances,key=lambda d:d[2])
spare_points = list(range(len(coordinates)))
boxes = []
# 
while len(boxes) != 1 or len(spare_points) != 0:
    link = distances_sorted.pop(0)
    boxes_flat = [bs for b in boxes for bs in b]
    if link[0] in spare_points:
        spare_points.remove(link[0])
    if link[1] in spare_points:
        spare_points.remove(link[1])
                     
    if link[0] in boxes_flat and link[1] in boxes_flat:
        for b in boxes: 
            if link[0] in b:
                b0 = b
            if link[1] in b:
                b1 = b
        if b1 != b0:
            
            b0.extend(b1)
            boxes.pop(boxes.index(b1))
        
    elif link[0] in boxes_flat:
        for b in boxes: 
            if link[0] in b:
                b.append(link[1])
    
    elif link[1] in boxes_flat:
        for b in boxes: 
            if link[1] in b:
                b.append(link[0])
    # 
    else:
        new_box = [link[0],link[1]]
        boxes.append(new_box)
# 
old_distances = sorted(distances,key=lambda d:d[2])
p = old_distances[old_distances.index(link)]
x1 = coordinates[p[0]][0]
x2 = coordinates[p[1]][0]
# 
print(x2*x1)