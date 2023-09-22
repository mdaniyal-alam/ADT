size = int(input("Enter the size of the stack: "))
stack = [None] * size
top = -1


def push(value):
    global stack, top
    if top == len(stack) - 1:
        print("Stack Overflow")
    else:
        top += 1
        stack[top] = value


def pop():
    global stack, top
    if top == -1:
        print("Stack Underflow")
    else:
        value = stack[top]
        top -= 1
        return value


while True:
    print("1. Push")
    print("2. Pop")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = input("Enter the data you want to push: ")
        push(value)
    elif choice == 2:
        value = pop()
        if value is not None:
            print("The popped data is: ", value)
    elif choice == 3:
        break
    else:
        print("The choice is invalid, try again: ")





