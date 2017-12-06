import time

start = time.time()

with open('input.txt', 'r') as f:
    content = f.read().split('\t')

memory_banks = [int(x) for x in content]

configs = []
done = False
while not done:

	if(str(memory_banks) not in configs):
		configs.append(str(memory_banks))
	else:
		done = True
		print "Done: %d, %d" % (len(configs), len(configs) - configs.index(str(memory_banks)))

	maxval = max(memory_banks)
	startpos = 0
	
	for i in range(0,len(memory_banks)):
		if(memory_banks[i] == maxval):
			startpos = i
			break
	
	dataamount = memory_banks[startpos]
	memory_banks[startpos] = 0

	for x in range(1, dataamount + 1):
		memory_banks[(startpos + x) % len(memory_banks)] += 1

end = time.time()
print(end - start)