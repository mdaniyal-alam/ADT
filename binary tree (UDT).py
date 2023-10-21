class btnode():
    def __init__(self):
        self.lp = -1
        self.data = -1
        self.rp = -1


bt = [btnode() for i in range(6)]
free = 0


def insertbt(value):
    global free
    if free == 6:
        print("Overflow")
    elif free == 0:
        bt[free].data = value
        free += 1
    else:
        newnode = free
        bt[newnode].data = value
        free += 1
        currnode = 0
        direction = ""
        while currnode != -1:
            prevnode = currnode
            if value < bt[currnode].data:
                currnode = bt[currnode].lp
                direction = "L"
            else:
                currnode = bt[currnode].rp
                direction = "R"
        if direction == "L":
            bt[prevnode].lp = newnode
        else:
            bt[prevnode].rp = newnode


insertbt(15)
insertbt(8)
insertbt(23)
insertbt(9)
insertbt(30)
insertbt(14)


print("LP\tDATA\tRP")
for i in range(6):
    print(f"{bt[i].lp}\t{bt[i].data}\t{bt[i].rp}\t")