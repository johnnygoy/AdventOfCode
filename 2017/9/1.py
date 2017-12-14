with open('input.txt', 'r') as f:
    content = f.read().strip()

depth = 0
score = 0

i = 0
in_garbage = False
garbage_count = 0

while i < len(content):
    if(content[i] == "!"):
        i += 2
        continue
    if(not in_garbage):
        if(content[i] == "<"):
            in_garbage = True
        elif(content[i] == "{"):
            depth += 1
            score += depth
        elif(content[i] == "}"):
            depth -= 1
    else:
        if(content[i] == ">"):
            in_garbage = False
        else:
            garbage_count += 1
    i += 1

print "Score: %d" % score
print "Garbage count: %d" % garbage_count
