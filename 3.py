import math

with open("3.input.txt", "r") as f:
    lines = [list(line.rstrip()) for line in f.readlines()]

latmove = 1
longmove = 2
slopes = ((1,1),(3,1),(5,1),(7,1),(1,2))

def run_slope(latmove, longmove):
    x, y, trees = 0, 0, 0
    height = len(lines)
    width = len(lines[0])
    while y < height:
        if y + longmove >= height:
            return trees
        else:
            y += longmove
        if x + latmove >= width:
            x = (x + latmove) - width
        else:
            x += latmove
        if lines[y][x] == "#":
            trees += 1
    return trees

totals = [run_slope(right,down) for right, down in slopes]

print(f"{math.prod(totals)}")
