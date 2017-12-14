def main():
    with open('input.txt', 'r') as f:
        content = f.read().split(',')

    directions = {
        'nw': [-1, 0, 1],
        'n': [-1, 1, 0],
        'ne': [0, 1, -1],
        'se': [1, 0, -1],
        's': [1, -1, 0],
        'sw': [0, -1, 1],
    }

    startpos = [0, 0, 0]
    current_pos = startpos
    distances = []

    for move in content:
        current_pos = make_move(current_pos, directions[move])
        distances.append(max([abs(x) for x in get_distance(startpos, current_pos)]))

    print distances[-1]
    print max(distances)


def make_move(current_pos, move):
    return [x + y for x, y in zip(current_pos, move)]


def get_distance(from_pos, to_pos):
    return [x - y for x, y in zip(from_pos, to_pos)]


main()
