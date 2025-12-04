def reach_paper_rolls(paper_grid):
    count = 0
    rows = len(paper_grid)
    cols = len(paper_grid[0])
    # 
    for i,row in enumerate(paper_grid):
        for j,el in enumerate(row):
            if el == '.':
                continue
            if i%139 == 0 and j%139 == 0:
                count += 1
                continue
            #
            neighbour_count = 0
            i_min = i - 1 if i -1 >= 0  else i 
            i_max = i + 2 if i + 2 <= rows else i + 1 
            for ip in range(i_min,i_max):
                j_min = j - 1 if j -1 >= 0  else j 
                j_max = j + 2 if j + 2 <= cols else j + 1
                for jp in range(j_min,j_max):
                    if ip == i and jp == j:
                        continue
                    if paper_grid[ip][jp] != '.':
                        neighbour_count += 1
            if neighbour_count < 4:
                count += 1
                paper_grid[i][j] = 'x'
    # 
    return count,paper_grid

def replace_x(paper_grid):
    for i,row in enumerate(paper_grid):
        for j,el in enumerate(row):
            if paper_grid[i][j] == 'x':
                paper_grid[i][j] = '.'
    return paper_grid

paper_grid = []
with open('input.txt','r') as file:
    for row in file:
        row = row.replace("\n","")
        paper_grid.append([element for element in row])



# first iteration
total_count,paper_grid = reach_paper_rolls(paper_grid)
paper_grid = replace_x(paper_grid)
print(f'Answer to the first part is {total_count}')
# 
# next iterations
partial_count = 1
while partial_count != 0:
    partial_count,paper_grid = reach_paper_rolls(paper_grid)
    paper_grid = replace_x(paper_grid)
    total_count += partial_count

print(f'Answer to the second part is {total_count}')