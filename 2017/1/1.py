f = open('input.txt', 'r')
puzzle_input = f.read()

total = 0
last_int = puzzle_input[-1:]
for i in puzzle_input:
    if(i == last_int):
        total += int(i)
    last_int = i

print total
