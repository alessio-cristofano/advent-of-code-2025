from typing import List

class BeamLine:
    state: List[int]
    next_layer: List[bool]
    split_count: int
    multiverse_count: int
    def read_line(self,string_line: List[str]):
        return [t != '.' for t in string_line]

    def __init__(self,state,next_layer):
        self.state = [int(t != '.') for t in state]
        self.next_layer = self.read_line(next_layer)
        self.split_count = 0
        self.multiverse_count = 0

    def split(self):
        for i,el in enumerate(self.next_layer):
            if el and self.state[i]:
                self.state[i-1] += self.state[i]
                self.state[i+1] += self.state[i]
                self.state[i] = 0
                self.split_count += 1
    def draw(self):
        print(''.join(['.' if not s else '^' for s in self.next_layer]))
        print(''.join([f'{s}' for s in self.state]))

parsed_file = []
with open("input.txt","r") as file:
    for row in file:
        row = row.replace("\n","")
        line = [r for r in row]
        parsed_file.append(line)

beam = BeamLine(parsed_file[0],parsed_file[1])
beam.split()
for line in parsed_file[2:]:
    beam.next_layer = beam.read_line(line)
    beam.split()

print(f'Solution of part 1 is {beam.split_count}')
print(f'Solution of part 2 is {sum(beam.state)}')