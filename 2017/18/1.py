import string

registers = {}
for c in string.ascii_lowercase:
	registers[c] = 0

last_sound = 0
position = 0

def main():
	global position
	global registers
	with open('input.txt', 'r') as f:
		content = f.readlines()

	instructions = []

	for line in content:
		instructions.append([x.strip() for x in line.split(" ")])

	found = False
	while not found:
		instruction = instructions[position]
		add_to_position = True
		if(instruction[0] == 'snd'):
			snd(instruction[1])
		if(instruction[0] == 'set'):
			set(instruction[1], instruction[2])
		if(instruction[0] == 'add'):
			add(instruction[1], instruction[2])
		if(instruction[0] == 'mul'):
			mul(instruction[1], instruction[2])
		if(instruction[0] == 'mod'):
			mod(instruction[1], instruction[2])
		if(instruction[0] == 'rcv'):
			found = rcv(instruction[1])
		if(instruction[0] == 'jgz'):
			add_to_position = jgz(instruction[1], instruction[2])
			#print "Jump %d" % instruction[1]
		
		if(add_to_position):
			position += 1


def snd(x):
	global registers
	global last_sound

	last_sound = get_val(x)
	

def set(x, y):
	global registers

	registers[x] = get_val(y)
	

def add(x, y):
	global registers

	registers[x] += get_val(y)
	

def mul(x, y):
	global registers

	registers[x] *= get_val(y)
	

def mod(x, y):
	global registers

	registers[x] %= get_val(y)
	

def rcv(x):
	global registers
	global last_sound

	if(get_val(x) != 0):
		print last_sound
		return True
	return False
	

def jgz(x, y):
	global registers
	global position

	if(get_val(x) > 0):
		position += get_val(y)
		return False
	return True

def get_val(x):
	global registers
	if(str(x) in string.ascii_lowercase):
		return int(registers[x])
	else:
		return int(x)
	

main()