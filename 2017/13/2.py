def main():

    with open('input.txt', 'r') as f:
        content = f.readlines()

    firewall = {}

    for c in content:
        firewall[int(c.split(": ")[0])] = int(c.split(": ")[1])

    number_of_elements = int(content[-1].split(": ")[0]) + 1

    startsecond = 0
    complete = False
    while not complete:
        complete = True
        for second in range(0,number_of_elements):
            the_range = firewall.get(second)
            if(the_range is not None and scanner_in_top_pos(second + startsecond, the_range)):
                complete = False
                break
        if(complete):
            print "Safe startsecond: %d" % startsecond
            break
        startsecond += 1


def scanner_in_top_pos(second, layer_range):
    return (second % (layer_range * 2 - 2) == 0)

main()