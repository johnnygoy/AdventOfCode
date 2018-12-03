fname = 'input.txt'
with open(fname) as f:
    content = f.readlines()

squares = []
for l in content:
    l = l.strip()
    str_parts = l.split(' ')
    square = {
        'id': str_parts[0][1:],
        'x': int(str_parts[2].split(',')[0]),
        'y': int(str_parts[2].split(',')[1][:-1]),
        'w': int(str_parts[3].split('x')[0]),
        'h': int(str_parts[3].split('x')[1]),
    }
    squares.append(square)

keys = {}
for square in squares:
    for y in range(square['y'], square['y'] + square['h']):
        for x in range(square['x'], square['x'] + square['w']):
            key = str(x) + ',' + str(y)
            if key not in keys:
                keys[key] = [square['id']]
            else:
                keys[key].append(square['id'])

for square in squares:
    overlaps = False
    for y in range(square['y'], square['y'] + square['h']):
        for x in range(square['x'], square['x'] + square['w']):
            key = str(x) + ',' + str(y)
            if not len(keys[key]) == 1:
                overlaps = True
    if not overlaps:
        print(square['id'])
