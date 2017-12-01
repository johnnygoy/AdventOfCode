f = open('input.txt', 'r')
puzzle_input = f.read()

total = 0
j = 0
for i in puzzle_input:
    index_to_compare = (j + (len(puzzle_input) / 2)) % len(puzzle_input)
    if(puzzle_input[index_to_compare] == i):
        total += int(i)

    j += 1

print total
