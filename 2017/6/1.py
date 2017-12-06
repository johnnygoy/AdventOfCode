fname = 'input.txt'
with open(fname) as f:
    content = f.readlines()

total = 0
for l in content:
    vals = l.strip().split("\t")

intvals = []
for val in vals:
	intvals.append(int(val))

configs = []
done = False
while not done:

	if(configs.count(str(intvals)) == 0):
		configs.append(str(intvals))
	else:
		done = True
		print "Done: %d, %d" % (len(configs), len(configs) - configs.index(str(intvals)))

	maxval = max(intvals)
	startpos = 0
	
	for i in range(0,len(intvals)):
		if(intvals[i] == maxval):
			startpos = i
			break
	
	dataamount = intvals[startpos]
	intvals[startpos] = 0

	for x in range(1, dataamount + 1):
		intvals[(startpos + x) % len(intvals)] += 1