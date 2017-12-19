line = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']

def main():
	with open('input.txt', 'r') as f:
	    content = f.read().split(",")

	base = ''.join(line)
	current = ''
	dances = 1000000000
	count = 0

	while(base != current):
		dance(content)
		current = ''.join(line)
		if(count == 0):
			print 'After first: ' + current
		count += 1

	dances = dances % count

	for i in range(dances):
		dance(content)

	print 'After one billion: ' + ''.join(line)


def dance(movelist):
	for move in movelist:
		if(move[0] == 's'):
			spin(int(move[1:]))
		if(move[0] == 'x'):
			parts = move[1:].split('/')
			exchange(int(parts[0]), int(parts[1]))
		if(move[0] == 'p'):
			parts = move[1:].split('/')
			partner(parts[0], parts[1])


def spin(x):
	global line

	neworder = line[-x:]
	neworder.extend(line[:-x])
	line = neworder


def exchange(pos_a, pos_b):
	global line

	neworder = line[:]
	neworder[pos_a] = line[pos_b]
	neworder[pos_b] = line[pos_a]
	line = neworder


def partner(name_a, name_b):
	exchange(line.index(name_a), line.index(name_b))


main()