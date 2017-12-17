def main():
	steps = 366

	current_position = 0
	circular_buffer = [0]

	for i in range(2017):
		next_position = (current_position + steps) % len(circular_buffer)
		circular_buffer.insert(next_position + 1,i + 1)
		current_position = next_position + 1

	print circular_buffer[circular_buffer.index(2017) + 1]

main()