fname = 'input.txt'
with open(fname) as f:
	content = f.readlines()

line = 0
for l in content:
	l = l.strip()
	
	for x in xrange(line,len(content)):
		diff = 0
		pos = 0
		for letter in l:
			if(letter != content[x][pos]):
				diff += 1
			pos += 1

		if(diff == 1):
			print(l)
			print(content[x])
			print('diff: ' + str(diff))
			print('--')
			return

	line += 1
