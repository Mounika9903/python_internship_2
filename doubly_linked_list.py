# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None

# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None
#     def insert_at_beginning(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         new_node.next = self.head
#         self.head.prev = new_node
#         self.head = new_node
#     def insert_at_end(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         temp = self.head
#         while temp.next:
#             temp = temp.next
#         temp.next = new_node
#         new_node.prev = temp
#     def insert_after(self, key, data):
#         temp = self.head
#         while temp and temp.data != key:
#             temp = temp.next
#         if temp is None:
#             print(f"Node with data {key} not found.")
#             return
#         new_node = Node(data)
#         new_node.next = temp.next
#         new_node.prev = temp
#         if temp.next:
#             temp.next.prev = new_node
#         temp.next = new_node
#     def delete_node(self, key):
#         temp = self.head
#         while temp and temp.data != key:
#             temp = temp.next
#         if temp is None:
#             print(f"Node with data {key} not found.")
#             return
#         if temp.prev:
#             temp.prev.next = temp.next
#         if temp.next:
#             temp.next.prev = temp.prev
#         if temp == self.head:
#             self.head = temp.next
#         del temp
#     def search(self, key):
#         temp = self.head
#         while temp:
#             if temp.data == key:
#                 return True
#             temp = temp.next
#         return False
#     def traverse_forward(self):
#         temp = self.head
#         while temp:
#             print(temp.data, end=" <-> ")
#             temp = temp.next
#         print("None")
#     def traverse_backward(self):
#         temp = self.head
#         if temp is None:
#             return
#         while temp.next:
#             temp = temp.next
#         while temp:
#             print(temp.data, end=" <-> ")
#             temp = temp.prev
#         print("None")

# dll = DoublyLinkedList()
# dll.insert_at_end(10)
# dll.insert_at_end(20)
# dll.insert_at_beginning(5)
# dll.insert_after(10, 15)
# dll.traverse_forward() 
# dll.traverse_backward()  
# dll.delete_node(10)
# dll.traverse_forward()  
# print("Search 15:", dll.search(15))  
# print("Search 100:", dll.search(100))

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length // 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
print("Popped node:", dll.pop().data if dll.pop() else None)
dll.prepend(5)
print("First node:", dll.head.data if dll.head else None)
print("Last node:", dll.tail.data if dll.tail else None)
print("Get index 1:", dll.get(1).data if dll.get(1) else None)