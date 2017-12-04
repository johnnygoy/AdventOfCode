fname = 'input.txt'
with open(fname) as f:
    content = f.readlines()

total = 0
for l in content:
    vals = l.strip().split(" ")
    valid = True
    for i in range(0, len(vals), 1):
        for j in range(i + 1, len(vals), 1):
            if(len(vals[i]) == len(vals[j])):
                has_anagram = True
                for c in vals[i]:
                    if(vals[i].count(c) != vals[j].count(c)):
                        has_anagram = False
                if(has_anagram):
                    valid = False

    if(valid):
        total += 1

print total