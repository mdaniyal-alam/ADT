class node():
    def __init__(self):
        self.data = -1
        self.next = -1


queue = [node() for i in range(6)]
tail, head = -1, -1
free = 0


def init_queue():
    for i in range(6):
        queue[i].next = i + 1
    queue[5].next = -1


def enqueue(value):
    global tail, head, free
    if tail == len(queue) - 1:
        print("Overflow")
    else:
        queue[tail + 1].data = value
        queue[tail].next = tail + 1
        tail += 1
        free = queue[tail].next
        if head == -1:
            head = 0


def dequeue():
    global tail, head, free
    if head == -1 or head > tail:
        print("Underflow")
    else:
        value = queue[head].data
        free = head
        head = queue[head].next
        if head is None:
            head = -1
            tail = -1
        return value


# main program

while True:
    print('1. Enqueue')
    print('2. Dequeue')
    print('3. Exit')

    choice = int(input("Enter your choice: "))
    if choice == 1:
        val = input("Enter the value to enqueue: ")
        enqueue(val)
    elif choice == 2:
        res = dequeue()
        print("Dequeued value: ", res)
    else:
        print("Exiting")
        break


