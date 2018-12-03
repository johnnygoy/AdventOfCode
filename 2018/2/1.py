fname = 'input.txt'
with open(fname) as f:
    content = f.readlines()

total = 0
twos = 0
threes = 0
for l in content:
    l = l.strip()
    two_count = False
    three_count = False
    for letter in l:
        if(l.count(letter) == 2):
            two_count = True
        if(l.count(letter) == 3):
            three_count = True
    if(two_count):
        twos += 1
    if(three_count):
        threes += 1

print twos * threes
