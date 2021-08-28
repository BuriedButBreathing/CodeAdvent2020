filepath = "C:\\users\\higgi\\onedrive\\documents\\github\\codeadvent2020\\question3\\input.txt"

with open(filepath) as r:
    slope_map = r.readlines()
    slope_map = [line.strip() for line in slope_map]
tree_count = 0
row, column = 0,0

while row+1 < len(slope_map):
    row += 2
    column += 1

    space = slope_map[row][column % len(slope_map[row])]
    if space == "#":
        tree_count += 1
print(tree_count)


# Part 2

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]


total = 1
for slope in slopes:
    tree_count = 0
    row, column = 0,0

    while row+1 < len(slope_map):
        row += slope[1]
        column += slope[0]

        space = slope_map[row][column % len(slope_map[row])]
        if space == "#":
            tree_count += 1
    total *= tree_count
print(total)
