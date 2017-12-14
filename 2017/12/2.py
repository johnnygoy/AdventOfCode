def main():
    with open('input.txt', 'r') as f:
        content = f.readlines()

    structure = []
    doors_left = []

    count = 0
    for line in content:
        structure.append([int(x) for x in line.split(' <-> ')[1].split(', ')])
        doors_left.append(count)
        count += 1

    groups = []

    while(len(doors_left) > 0):
        connections = structure[doors_left[0]]

        start_group_size = 0
        last_group_size = len(connections)

        while (start_group_size != last_group_size):
            start_group_size = len(connections)

            new_connections = []

            for door in connections:
                new_connections.extend(structure[door])
                for i in range(0, len(doors_left)):
                    if(door in structure[doors_left[i]]):
                        new_connections.append(doors_left[i])

            connections.extend(new_connections)
            connections = list(set(connections))

            last_group_size = len(connections)

        for connection in connections:
            doors_left.remove(connection)

        groups.append(connections)

    print len(groups)

main()
