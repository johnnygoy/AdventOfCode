fname = 'example.txt'
with open(fname) as f:
    content = f.readlines()

total = 0
for l in content:
    vals = l.strip().split("\t")
    vals = [int(i) for i in vals]

    for i in range(0, len(vals), 1):
    	for j in range(i + 1, len(vals), 1):
    		if(vals[i] % vals[j] == 0):
    			total += vals[i] / vals[j]
    		elif(vals[j] % vals[i] == 0):
    			total += vals[j] / vals[i]

print total
