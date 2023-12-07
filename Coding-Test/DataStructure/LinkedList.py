class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = Nonkke

    def append(self, value):
        new_node =  Node(value)

        if self.head is None:
            self.head= new_node
            self.tail= new_node

        self.tail.next = new_node
        self.tail = new_node