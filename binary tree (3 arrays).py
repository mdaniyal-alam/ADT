data = [None for i in range(6)]
lp = [None for j in range(6)]
rp = [None for k in range(6)]

# initialization
for i in range(6):
    data[i] = -1
    lp[i] = -1
    rp[i] = -1
free = 0


def insertbt(value):
    global free
    if free == 6:
        print("Overflow")
    elif free == 0:
        data[free] = value
        free += 1
    else:
        newnode = free
        data[newnode] = value
        free += 1
        currnode = 0
        direction = ""
        while currnode != -1:
            prevnode = currnode
            if value < data[currnode]:
                currnode = lp[currnode]
                direction = "L"
            else:
                currnode = rp[currnode]
                direction = "R"
        if direction == "L":
            lp[prevnode] = newnode
        else:
            rp[prevnode] = newnode


insertbt(15)
insertbt(8)
insertbt(23)
insertbt(9)
insertbt(30)
insertbt(14)


print("LP\tDATA\tRP")
for i in range(6):
    print(f"{lp[i]}\t{data[i]}\t{rp[i]}")


