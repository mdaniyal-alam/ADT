Q = [None for i in range(10)]
tail = 0
head = 0
Qlen = len(Q)
Qsize = 0


def init_queue():
    global tail, head, Qlen, Qsize
    tail = -1
    head = -1
    Qsize = 0
    for i in range(Qlen):
        Q[i] = ""


def enqueue(value):
    global tail, Qsize
    if Qsize == Qlen:
        print("Overflow")
    elif tail == Qlen - 1:
        tail = 0
    else:
        tail += 1
    Q[tail] = value
    Qsize += 1


def dequeue():
    global head, Qsize
    if Qsize == 0:
        print("Underflow")
    elif head == Qlen - 1:
        head = 0
    else:
        head += 1
    Qsize -= 1
    return Q[head]

choice = -1
while choice != 5:
    print("1. Initialize")
    print("2. Enqueue")
    print("3. Dequeue")
    print("4. Output")
    print("5. Exit")
    choice = int(input("Please enter your choice: "))

    if choice == 1:
        init_queue()
    elif choice == 2:
        value = input("Please enter the value: ")
        enqueue(value)
    elif choice == 3:
        value = dequeue()
        print(value)
    elif choice == 4:
        print(Q)
    elif choice == 5:
        print("Exiting...")
    else:
        print("Choice is invalid!")



