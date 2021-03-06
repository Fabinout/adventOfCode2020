import re


class bag:
    qty = []
    child = []
    containGold = False

    def __init__(self, str):
        self.qty = []
        self.child = []
        self.color = str[0]
        for b in str[1:len(str)]:
            if (re.search("no other", b) != None):
                break
            self.qty.append(int(b[0]))
            self.child.append(b[2:len(b)])

    def contains(self, collection, toplevel):

        out = 1
        if (toplevel):
            out = 0
        if len(self.qty) == 0:
            return 1
        for i in range(len(self.qty)):
            for b in collection:
                if (b.color == self.child[i]):
                    out += self.qty[i] * b.contains(collection, False)
                    break
        return out

    def define(self):
        print(self.color)
        print("->")
        print(len(b.child))
        for i in range(len(self.qty)):
            print(self.child[i])


def find_container(collection, color):
    for b_item in collection:
        for bc in b_item.child:
            if (bc == color and not b_item.containGold):
                b_item.containGold = True
                find_container(collection, b_item.color)


file = open("original_input.txt")
str = file.readline()
bags = []

while (str):
    str = re.split(" bags contain | bag, | bags, ", str)
    str[-1] = re.sub(" bags.\n| bag.\n", '', str[-1])
    bags.append(bag(str))
    str = file.readline()
find_container(bags, "shiny gold")
out = 0
out2 = 0
for b in bags:
    if (b.color == "shiny gold"):
        out2 = b.contains(bags, True)
    if (b.containGold):
        out += 1

print("part 1: ", out)
print("part 2: ", out2)
