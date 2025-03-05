class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            last = self.head.prev
            last.next = new_node
            new_node.prev = last
            new_node.next = self.head
            self.head.prev = new_node

    def delete(self, key):
        if not self.head:
            return
        temp = self.head
        while True:
            if temp.data == key:
                if temp.next == temp:  
                    self.head = None
                    return
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                if temp == self.head:
                    self.head = temp.next
                return
            temp = temp.next
            if temp == self.head:
                break

    def search(self, key):
        if not self.head:
            return False
        temp = self.head
        while True:
            if temp.data == key:
                return True
            temp = temp.next
            if temp == self.head:
                return False

    def display(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" <-> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(head)")


dcll = DoublyCircularLinkedList()
dcll.insert(10)
dcll.insert(20)
dcll.insert(30)
dcll.display()
print("Search 20:", dcll.search(20))
dcll.delete(20)
dcll.display()