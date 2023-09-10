def run_01():
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    class Queue:
        def __init__(self):
            self.front = None
            self.tail = None

        def is_empty(self):
            if self.front is None:
                return None

        def enqueue(self, data):
            new_node = Node(data)
            if self.tail is None:
                self.front = new_node
                self.tail = new_node
                return
            self.tail.next = new_node
            self.tail = new_node

        def dequeue(self):
            if self.is_empty():
                print("Queue is empty")
            dequeued_data = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.tail = None
            return dequeued_data

        def check(self):
            if self.is_empty():
                print("Queue is empty")
            return self.front.data

        def display(self):
            current = self.front
            while current:
                print(current.data)
                current = current.next
            print("No more queue")

    def run():
        queue = Queue()
        queue.enqueue(5)
        queue.enqueue(10)
        queue.enqueue(15)
        queue.enqueue(20)
        queue.display()
        queue.dequeue()
        queue.dequeue()
        queue.display()

    print(run())


def run_02():
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    class Stack:
        def __init__(self):
            self.top = None

        def is_empty(self):
            return self.top is None

        def push(self, data):
            new_node = Node(data)
            new_node.next = self.top
            self.top = new_node

        def pop(self):
            if self.is_empty():
                return ("Stack is empty")
            popped_data = self.top.data
            self.top = self.top.next
            return popped_data

        def check(self):
            if self.is_empty():
                print("Stack is empty")
            return self.top.data

        def display(self):
            current = self.top
            while current:
                print(current.data)
                current = current.next
            print("No more stack")

    def run():
        stack = Stack()
        stack.push(5)
        stack.push(10)
        stack.push(15)
        stack.push(20)
        stack.display()

    print(run())
