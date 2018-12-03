fname = 'input.txt'
with open(fname) as f:
    content = f.readlines()

freq = 0
for l in content:
    if(l[0] == '+'):
        freq += int(l[1:])
    else:
        freq -= int(l[1:])

print freq
