
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:

    def __init__(self):
        self.tail = None
        self.head = None

    def add(self, value):
        if not isinstance(value, Node):
            value = Node(value)

        if self.head is None:
            self.head = value
            self.tail = value
        else:
            self.tail.next = value
            self.tail = value



    def pop(self):
        if self.head is None:
            return None
        element = self.head
        self.head = self.head.next
        return element.value

    def peek(self):
        if self.head is None:
            return None
        return self.head.value

    def search(self, value):
        if self.head is None:
            return "Element not found"
        current_el = self.head
        index = 0
        while current_el:
            if current_el.value == value:
                return f"{value} found at index {index}"
            index +=1
            current_el = current_el.next
        return "Element not found"



    def __str__(self):
        if self.head is None:
            return "Queue is empty"
        else:
            output = ""
            current_element = self.head
            while current_element:
                output = current_element.value + "->" + output
                current_element = current_element.next
            return output

myQueue = Queue()
myQueue.add("Samuel")
myQueue.add("Julie")
myQueue.add("Nicole")
myQueue.add("John")
myQueue.add("Elon")
myQueue.add("Ben")
print(myQueue.search("Samuel"))

#myQueue.pop()
#print(myQueue.peek())
print(myQueue)
