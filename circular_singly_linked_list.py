class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def delete(self, key):
        if not self.head:
            return
        temp = self.head
        prev = None
        while True:
            if temp.data == key:
                if prev:
                    prev.next = temp.next
                else:
                    if temp.next == self.head:
                        self.head = None
                    else:
                        self.head = temp.next
                        last = self.head
                        while last.next != temp:
                            last = last.next
                        last.next = self.head
                return
            prev = temp
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
                break
        return False

    def display(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(head)")
cll = CircularLinkedList()
cll.insert(10)
cll.insert(20)
cll.insert(30)
cll.display()
print("Search 20:", cll.search(20))
cll.delete(20)
cll.display()
print("Search 20 after deletion:", cll.search(20))                              
                    