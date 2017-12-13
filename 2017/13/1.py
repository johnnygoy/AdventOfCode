def main():
	with open('input.txt', 'r') as f:
	    content = f.readlines()

	firewall = {}

	second = 0
	damage = 0

	for c in content:
		firewall[int(c.split(": ")[0])] = int(c.split(": ")[1])

	while(second < 100):
		if(firewall.get(second) != None):
			if(scanner_in_top_pos(second, firewall[second])):
				damage += second * firewall[second]
				print "Hit in layer: %d with range %d" % (second, firewall[second])
		second += 1
	#print firewall
	print damage


def scanner_in_top_pos(second, layer_range):
	return (second % (layer_range * 2 - 2) == 0)

main()