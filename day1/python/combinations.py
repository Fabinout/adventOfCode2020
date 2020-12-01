from itertools import combinations

with open('2020_01.txt') as f:
    data = f.readlines()

data = [row.rstrip() for row in data]

def part1(data):
    for x,y in combinations(data, 2):
        if int(x) + int(y) == 2020:
            answer = int(x)*int(y)
            return answer

def part2(data):
    for x,y,z in combinations(data, 3):
        if int(x) + int(y) + int(z) == 2020:
            answer = int(x)*int(y)*int(z)
            return answer

print(part1(data))
print(part2(data))
