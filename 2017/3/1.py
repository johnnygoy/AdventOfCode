import math

number = 361527

square_size = math.sqrt(number)

print "-- %d --" % number
prev_square = int(square_size)
if(not number % square_size):
	prev_square -= 1
if(not prev_square % 2):
	prev_square -= 1

steps_left = number - (prev_square * prev_square)
current_side = prev_square + 2
max_steps = (current_side - 1) / 2
side_steps = abs(max_steps - (steps_left % (current_side - 1)))
total_steps = side_steps + (current_side / 2)

print total_steps