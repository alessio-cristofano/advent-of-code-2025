from math import prod
full_input = []
with open("input.txt","r") as file:
    for row in file:
        row_input = [r for r in row.replace('\n','').split(" ") if r != '']
        full_input.append(row_input)
# 
solution = 0
for col_number in range(len(full_input[0])):
    if full_input[-1][col_number] == '*':
        partial = 1
        for row_number in range(len(full_input) - 1):
            partial = partial*int(full_input[row_number][col_number])
    else: 
        partial = 0
        for row_number in range(len(full_input) - 1):
            partial = partial + int(full_input[row_number][col_number])
    solution += partial

print(f"Solution to part 1 is {solution}")

# Part 2
#
solution2 = 0
with open("input.txt","r") as file:
    input_problem2 = [l for l in file.read().split('\n') if len(l)!= 0]

current_numbers = []
operation = print
for col in range(len(input_problem2[0])):
    #
    op = input_problem2[-1][col] 
    number = ''   
    match op:
        case ' ':
            pass
        case '*':
            operation = prod
            # print(op)
        case '+':
            operation = sum
            # print(op)
    for row in range(len(input_problem2) - 1):
        number += input_problem2[row][col]
    
    # input()
    if len(number.strip()) == 0:
        solution2 += operation(current_numbers)
        current_numbers = []
        continue
    current_numbers.append(int(number.strip()))

    if col == len(input_problem2[0])-1:
        solution2 += operation(current_numbers)

print(f"Solution to part 2 is {solution2}")