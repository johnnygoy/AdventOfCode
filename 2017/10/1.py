def main():
    with open('input.txt', 'r') as f:
        content = f.read().split(',')

    twists = [int(x) for x in content]

    string = [x for x in range(0,256)]

    pos = 0
    skip = 0

    for move in twists:
        print "Twist from %d with length %d:" % (pos % len(string), move)
        twist(pos, move, string)
        pos += move + skip
        skip += 1

    print string[0] * string[1]


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


main()
