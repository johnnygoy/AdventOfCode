fname = 'input.txt'
with open(fname) as f:
    content = f.readlines()

total = 0
for l in content:
    vals = l.strip().split("\t")
    vals = [int(i) for i in vals]

    total += max(vals) - min(vals)

print total
