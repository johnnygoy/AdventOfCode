
def main():
    fname = 'input.txt'
    with open(fname) as f:
        content = f.readlines()

    programs = []

    # Initiate all towers
    for l in content:

        parts = l.strip().split(" -> ")
        towername = parts[0].split(" (")[0]
        towerweight = parts[0].split(" (")[1].split(")")[0]

        temptower = Tower(towername, towerweight)

        programs.append(temptower)

    # Add proper structure
    for l in content:
        parts = l.strip().split(" -> ")
        towername = parts[0].split(" (")[0]

        if(len(parts) > 1):
            parentTower = None
            for program in programs:
                if(program.name == towername):
                    parentTower = program

            for part in parts[1].split(", "):
                for program in programs:
                    if(program.name == part):
                        parentTower.add_child(program)


    for program in programs:
        if(program.name == "eqgvf"):
            program.set_level(0)
            program.get_weight()

    for program in programs:
        checkweight = 0
        if(len(program.children) > 0):
            checkweight = int(program.children[0].totalweight) # WTF MAN?!
            error = False
            for child in program.children:
                if(checkweight != int(child.totalweight)):  # WTF MAN?!
                    print "Error in: %s at level %d. You do the fucking math..." % (program.name, program.level)
                    error = True

            if(error):
                for child in program.children:
                    print child.name + ": " + str(child.totalweight) + " [" + child.weight + "]"


class Tower:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.totalweight = 0
        self.children = []
        self.level = 0

    def add_child(self, child):
        self.children.append(child)

    def get_weight(self):
        if(len(self.children) == 0):
            self.totalweight = self.weight
            return self.weight
        else:
            for child in self.children:
                self.totalweight += int(child.get_weight())
            self.totalweight += int(self.weight)
            return self.totalweight

    def set_level(self, level):
        level += 1
        self.level = level
        if(len(self.children) > 0):
            for child in self.children:
                child.set_level(level)

    def __str__(self):
        childstring = " -> "
        for child in self.children:
            childstring += child.name + "(" + str(child.weight) + ") [" + str(child.totalweight) + "], "
        return str(self.level) + ": " + self.name + "(" + str(self.weight) + ") [" + str(self.totalweight) + "] " + childstring

main()