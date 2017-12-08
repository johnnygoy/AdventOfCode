with open('input.txt', 'r') as f:
    content = f.readlines()

instructions = []
registers = {}

running_max_val = float("-inf")

for line in content:
    parts = line.split(" ")
    modifier = 1 if (parts[1] == 'inc') else -1
    instruction = {
        'register': parts[0].strip(),
        'amount': int(parts[2].strip()) * modifier,
        'register_to_compare': parts[4].strip(),
        'comparison': parts[5].strip(),
        'compare_to': int(parts[6].strip())
    }

    registers[instruction['register']] = 0
    instructions.append(instruction)

for instruction in instructions:
    comparison = False
    if(instruction['comparison'] == '=='):
        comparison = registers[instruction['register_to_compare']] == instruction['compare_to']
    elif (instruction['comparison'] == '>='):
        comparison = registers[instruction['register_to_compare']] >= instruction['compare_to']
    elif (instruction['comparison'] == '>'):
        comparison = registers[instruction['register_to_compare']] > instruction['compare_to']
    elif (instruction['comparison'] == '<'):
        comparison = registers[instruction['register_to_compare']] < instruction['compare_to']
    elif (instruction['comparison'] == '<='):
        comparison = registers[instruction['register_to_compare']] <= instruction['compare_to']
    elif (instruction['comparison'] == '!='):
        comparison = registers[instruction['register_to_compare']] != instruction['compare_to']

    if(comparison):
        registers[instruction['register']] += instruction['amount']

    current_max = registers[max(registers, key=registers.get)]
    if(current_max > running_max_val):
        running_max_val = current_max

max_val = max(registers, key=registers.get)

print "Final max: %d" % registers[max_val]
print "Running max: %d" %  running_max_val
