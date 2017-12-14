def main():
    with open('input.txt', 'r') as f:
        content = f.readlines()

    structure = []

    for line in content:
        structure.append([int(x) for x in line.split(' <-> ')[1].split(', ')])

    connections = structure[0]

    start_group_size = 0
    last_group_size = len(connections)

    while (start_group_size != last_group_size):
        start_group_size = len(connections)

        new_connections = []

        for door in connections:
            new_connections.extend(structure[door])
            for i in range(0, len(structure)):
                if(door in structure[i]):
                    new_connections.append(i)

        connections.extend(new_connections)
        connections = list(set(connections))

        last_group_size = len(connections)

    print len(connections)


main()
