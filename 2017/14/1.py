def main():
	hash_input = "nbysizxe"
	test_hash_input = "flqrgnkx"

	used_input = hash_input

	rows = []
	for i in range(0, 128):
		row = used_input + "-" + str(i)
		row = get_knot_hash(row)
		complete_row = ''
		for c in row:
			complete_row += hex_to_bin(c)
		rows.append(complete_row)

	total = 0
	for row in rows:
		total += row.count('1')
	
	print total


def hex_to_bin(hex):
	scale = 16 ## equals to hexadecimal
	num_of_bits = 4

	return bin(int(hex, scale))[2:].zfill(num_of_bits)


def get_hex_str(intval):
    hex_str = str(hex(intval))[2:]
    if(len(hex_str) == 1):
        return "0" + hex_str
    return hex_str


def get_xor(intlist):
    prev = intlist[0]
    for i in range(1, len(intlist)):
        prev = prev ^ intlist[i]
    return prev


def twist(start, length, list_to_update):

    if(length == 0):
        return

    start_index = start % len(list_to_update)
    end_index = (start + length) % len(list_to_update)

    if(start_index >= end_index):
        templist = list_to_update[start_index:len(list_to_update)]
        templist.extend(list_to_update[0:end_index])
        templist = templist[::-1]
        for i in range(0,len(templist)):
            list_to_update[(start_index + i) % len(list_to_update)] = templist[i]

    else:
        list_to_update[start_index:length + start_index] = list_to_update[start_index:length + start_index][::-1]


def get_knot_hash(string_to_hash):
    base_addition_lengths = [17, 31, 73, 47, 23]

    sequence = []
    for c in string_to_hash:
        sequence.append(ord(str(c)))

    sequence.extend(base_addition_lengths)
    
    string = [x for x in range(0,256)]

    pos = 0
    skip = 0
    rounds = 64

    for i in range(0, rounds):
        for move in sequence:
            twist(pos, move, string)
            pos += move + skip
            skip += 1

    dense_hash = []
    step = 16
    for i in range(0, len(string), step):
        dense_hash.append(get_xor(string[i:i+step]))

    final_hash = ""
    for i in dense_hash:
        final_hash += get_hex_str(i)

    return final_hash


main()