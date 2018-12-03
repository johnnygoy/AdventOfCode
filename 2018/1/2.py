fname = 'input.txt'
with open(fname) as f:
    content = f.readlines()

freq = 0
duplicate_found = False
freqs = {}

while not duplicate_found:
    for l in content:
        if(l[0] == '+'):
            freq += int(l[1:])
        else:
            freq -= int(l[1:])

        if(freq in freqs):
            if not duplicate_found:
                print freq
            duplicate_found = True
        else:
            freqs[freq] = 1
