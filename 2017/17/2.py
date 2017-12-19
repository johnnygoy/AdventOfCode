def main():
	steps = 366
	current_position = 0
	length = 1
	
	last_value_after_zero = 0

	for i in range(50000000):
		next_position = (next_position + steps) % (i + 1)
		if(next_position == 0):
			last_value_after_zero = i + 1
		current_position = next_position + 1

	print last_value_after_zero

main()