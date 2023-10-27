class Node:
    def __init__(self):
        self.previous = None
        self.data = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.header = None  # 첫 번째 Node를 가리킴
        self.tail = None  # 마지막 Node를 가리킴

    def add(self, data):
        # 새로운 노드를 추가하고 값을 저장
        new_node = Node()
        new_node.data = data
        new_node.next = None

        if self.header is None:
            self.header = new_node
            self.tail= new_node

        self.tail.next = new_node
        self.tail = new_node

    def remove_last_node(self):





ll = LinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
print(ll.pointer.next)