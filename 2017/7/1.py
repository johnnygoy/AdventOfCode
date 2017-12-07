fname = 'input.txt'
with open(fname) as f:
    content = f.readlines()

all_programs = []
top_programs = []
for l in content:
    parts = l.strip().split(" -> ")
    all_programs.append(parts[0].split(" (")[0])
    if(len(parts) > 1):
        for part in parts[1].split(", "):
            top_programs.append(part)

print len(top_programs)
print len(all_programs)

for program in all_programs:
    if(program not in top_programs):
        print program