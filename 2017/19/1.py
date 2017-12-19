import string

position = (0,0)
direction = (0,0)
maze = []

def main():
	global position
	global direction
	global maze

	with open('input.txt', 'r') as f:
		content = f.readlines()

	for line in content:
		maze_line = []
		for c in line:
			maze_line.append(c)
		if(maze_line[-1] == '\n'):
			maze_line = maze_line[:-1]
		maze.append(maze_line)

	position = find_start()
	direction = (1,0)

	letters = ""
	count = 0

	while True:
		standing_on = walk()
		if(standing_on == "+"):
			change_direction()
		if(standing_on in string.ascii_uppercase):
			letters += standing_on

		count += 1

		if(standing_on == " "):
			break

	print "Number of steps: %d" % count
	print "Letters: %s" % letters


def find_start():
	global maze

	for i in range(len(maze[0])):
		if(maze[0][i] == "|"):
			return (0,i)


def walk():
	global maze
	global position
	global direction

	position = tuple(map(sum, zip(position, direction)))
	return maze[position[0]][position[1]]


def change_direction():
	global maze
	global position
	global direction

	if(direction[0] != 0):
		if(maze[position[0]][position[1] - 1] == "-" or maze[position[0]][position[1] - 1] in string.ascii_uppercase):
			direction = (0, -1)
		if(maze[position[0]][position[1] + 1] == "-" or maze[position[0]][position[1] + 1] in string.ascii_uppercase):
			direction = (0, 1)
	elif(direction[1] != 0):
		if(maze[position[0] - 1][position[1]] == "|" or maze[position[0] - 1][position[1]] in string.ascii_uppercase):
			direction = (-1, 0)
		if(maze[position[0] + 1][position[1]] == "|" or maze[position[0] + 1][position[1]] in string.ascii_uppercase):
			direction = (1, 0)


main()