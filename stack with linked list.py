class list():
    def __init__(self):
        self.data = -1
        self.next = -1


stack = [list() for i in range(6)]
head = -1
tail = -1
free = 0
for i in range(6):
    stack[i].next = i + 1
stack[5].next = -1


def push(value):
    global tail, free
    if tail == len(stack) - 1:
        print("Overflow")
    else:
        stack[tail + 1].data = value
        tail += 1
        free = stack[tail].next


def pop():
    global tail, free
    if tail == -1:
        print("Underflow")
    else:
        value = stack[tail].data
        tail -= 1
        free = stack[tail].next
        return value


# main program

while True:
    print('1. Push')
    print('2. Pop')
    print('3. Exit')

    choice = int(input("Enter your choice: "))
    if choice == 1:
        val = input("Enter the value to push: ")
        push(val)
    elif choice == 2:
        res = pop()
        print("Popped value is: ", res)
    else:
        print("Exiting")
        break


