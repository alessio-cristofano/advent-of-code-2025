from typing import List
from math import floor,sqrt
import numpy as np

def check_valid_id(id_string:str) -> bool: #true if valid
    # filter all the id_ranges with odd number of digits 
    length = len(id_string)
    factors = []
    for i in range(2,length+1):
        if length % i == 0:
            factors.append((i,int(length/i)))
    #
    for f in factors:
        f1 = f[0] # reps
        f2 = f[1] # number of digits
        
        if id_string == f1*id_string[0:f2] and f1==2:
            return False
    return True



id_ranges = []
with open('input.txt','r') as file:
    for row in file:
        parts = row.replace("\n","").split(',')
        for p in parts:
            id_ranges.append(p)

id_ranges = [
'67562556-67743658',
'62064792-62301480',
'4394592-4512674',
'3308-4582',
'69552998-69828126',
'9123-12332',
'1095-1358',
'23-48',
'294-400',
'3511416-3689352',
'1007333-1150296',
'2929221721-2929361280',
'309711-443410',
'2131524-2335082',
'81867-97148',
'9574291560-9574498524',
'648635477-648670391',
'1-18',
'5735-8423',
'58-72',
'538-812',
'698652479-698760276',
'727833-843820',
'15609927-15646018',
'1491-1766',
'53435-76187',
'196475-300384',
'852101-903928',
'73-97',
'1894-2622',
'58406664-58466933',
'6767640219-6767697605',
'523453-569572',
'7979723815-7979848548',
'149-216'
]



invalid_ids = []
for _range in id_ranges:
    start = int(_range.split('-')[0])
    end = int(_range.split('-')[1])

    for _id in range(start,end+1):
        if not check_valid_id(str(_id)):
            invalid_ids.append(_id)

print(np.sum(np.array(list(set(invalid_ids)))))
