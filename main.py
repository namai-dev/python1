class Stack:
    def __init__(self):
        self.data = []

    def isEmpty(self):
        if len(self.data) == 0:
            return True
        else:
            return False

    def top(self):
        if Stack.isEmpty(self):
            print("Stack is empty")
        else:
            print(f" Recently Added item {self.data[-1]}")

    def push(self, data):
        self.data.append(data)
        print("Added successfully")

    def pop(self):
        if Stack.isEmpty(self):
            print("Stack already empty..")
        else:
            self.data.pop(len(self.data) - 1)

    def current_size(self):
        print(f" Current size {len(self.data)}")

    def show_items(self):
        for i in range(len(self.data) - 1, -1, -1):
            print(self.data[i])


example = Stack()

example.push(9)
example.push(84)
example.push(48)
example.push(84)
example.push(38)
example.push(9)

example.show_items()

example.current_size()

example.top()

example.pop()

example.top()

print(example.isEmpty())
