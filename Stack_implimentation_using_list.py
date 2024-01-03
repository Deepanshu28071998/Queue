class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

def userDefinedFunction():
    stack = Stack()
    print("Enter a number:")
    print("1. Push to stack")
    print("2. Pop from stack")
    print("3. Peek the top of stack")
    print("4. Check if stack is empty")
    print("5. Print the size of stack")
    print("6. Exit")

    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            stack.push(int(input("Enter a number to push: ")))
        elif choice == 2:
            if stack.isEmpty():
                print("Stack is empty.")
            else:
                print(f"Popped: {stack.pop()}")
        elif choice == 3:
            if stack.isEmpty():
                print("Stack is empty.")
            else:
                print(f"Peek: {stack.peek()}")
        elif choice == 4:
            if stack.isEmpty():
                print("Stack is empty.")
            else:
                print("Stack is not empty.")
        elif choice == 5:
            print(f"Size of stack: {stack.size()}")
        elif choice == 6:
            break
        else:
            print("Invalid choice.")

userDefinedFunction()