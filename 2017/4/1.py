fname = 'input.txt'
with open(fname) as f:
    content = f.readlines()

total = 0
for l in content:
	vals = l.strip().split(" ")
	valid = True
	for val in vals:
		if(vals.count(val) > 1):
			valid = False
	if(valid):
		total += 1

print total