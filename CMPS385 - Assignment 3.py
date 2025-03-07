class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-2]

    def push(self, value):
        node = Node(value)
        node.next = self.head.next 
        self.head.next = node 
        self.size += 1

    def topAndPop(self):
        remove = self.head.next
        self.head.next = remove.next 
        self.size -= 1
        return remove.value

#Driver code
if __name__ == "__main__":
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)
    print(f"Stack: {stack}")

    for _ in range(1, 6):
        top_value = stack.topAndPop()
        print(f"Pop: {top_value}")
    print(f"Stack: {stack}")
