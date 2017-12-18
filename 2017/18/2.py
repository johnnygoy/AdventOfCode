import string


def main():
	with open('input.txt', 'r') as f:
		content = f.readlines()

	instructions = []

	for line in content:
		instructions.append([x.strip() for x in line.split(" ")])

	program1 = Program(0, instructions)
	program2 = Program(1, instructions)

	program1.receiving_program = program2
	program2.receiving_program = program1

	deadlock = False
	
	steps = 0

	count = 0
	
	while not deadlock:
		waiting2 = program2.step()
		waiting1 = program1.step()

		if(waiting1 and waiting2):
			deadlock = True

		count += 1

	print "Done"
	print str(program2.sent)


class Program:

	def __init__(self, id, instructions):
		self.registers = {}
		for c in string.ascii_lowercase:
			self.registers[c] = 0
		self.registers['p'] = id
		self.id = id
		self.receiving_program = None
		self.queue = []
		self.instructions = instructions
		self.position = 0
		self.sent = 0


	def step(self):
		
		instruction = self.instructions[self.position]
		add_to_position = True
		waiting = False

		if(instruction[0] == 'snd'):
			self.send_to_queue(instruction[1])
		if(instruction[0] == 'set'):
			self.set(instruction[1], instruction[2])
		if(instruction[0] == 'add'):
			self.add(instruction[1], instruction[2])
		if(instruction[0] == 'mul'):
			self.mul(instruction[1], instruction[2])
		if(instruction[0] == 'mod'):
			self.mod(instruction[1], instruction[2])
		if(instruction[0] == 'rcv'):
			add_to_position = self.read_from_queue(instruction[1])
			if(not add_to_position):
				waiting = True
		if(instruction[0] == 'jgz'):
			add_to_position = self.jgz(instruction[1], instruction[2])

		if(add_to_position):
			self.position += 1

		return waiting


	def receive_to_queue(self, val):
		self.queue.append(val)


	def send_to_queue(self, val):
		self.receiving_program.receive_to_queue(self.get_val(val))
		self.sent += 1


	def read_from_queue(self, register):
		if(len(self.queue) == 0):
			return False
		self.registers[register] = self.queue[0]
		self.queue = self.queue[1:]
		return True


	def set(self, x, y):
		self.registers[x] = self.get_val(y)
		

	def add(self, x, y):
		self.registers[x] += self.get_val(y)
		

	def mul(self, x, y):
		self.registers[x] *= self.get_val(y)
		

	def mod(self, x, y):
		self.registers[x] %= self.get_val(y)
		

	def jgz(self, x, y):
		if(self.get_val(x) > 0):
			self.position += self.get_val(y)
			return False
		return True


	def get_val(self, x):
		if(str(x) in string.ascii_lowercase):
			return int(self.registers[x])
		else:
			return int(x)


main()