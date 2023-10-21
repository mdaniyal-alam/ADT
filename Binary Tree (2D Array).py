bt = [[None for i in range(3)] for j in range(6)]
for i in range(6):
    bt[i][0] = -1
    bt[i][1] = -1
    bt[i][2] = -1

free = 0


def insertbt(value):
    global free
    if free == 6:
        print("Overflow")
    elif free == 0:
        bt[free][1] = value
        free += 1
    else:
        newnode = free
        bt[newnode][1] = value
        free += 1
        currnode = 0
        direction = ""
        while currnode != -1:
            prevnode = currnode
            if value < bt[currnode][1]:
                currnode = bt[currnode][0]
                direction = "L"
            else:
                currnode = bt[currnode][2]
                direction = "R"
        if direction == "L":
            bt[prevnode][0] = newnode
        else:
            bt[prevnode][2] = newnode


insertbt(15)
insertbt(8)
insertbt(23)
insertbt(9)
insertbt(30)
insertbt(14)

print("LP\tDATA\tRP")
for i in range(6):
    print(f"{bt[i][0]}\t{bt[i][1]}\t{bt[i][2]}\t")
