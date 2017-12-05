fname = 'input.txt'
with open(fname) as f:
    content = f.readlines()

intarr = []
for l in content:
	l = l.strip()
	intarr.append(int(l))

position = 0
steps = 0
try:
    while True:
    	newpos = position + intarr[position]
    	intarr[position] += 1
    	steps += 1
    	position = newpos
except IndexError:
    print "Done: %d" % steps
