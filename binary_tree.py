class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None
    def insert(self, data):
        if not self.root:
            self.root = Node(data)
            return
        queue = [self.root]
        while queue:
            temp = queue.pop(0)
            if not temp.left:
                temp.left = Node(data)
                return
            else:
                queue.append(temp.left)
            if not temp.right:
                temp.right = Node(data)
                return
            else:
                queue.append(temp.right)

    def get_root(self):
        return self.root

    def print_tree(self):
        if not self.root:
            print("Tree is empty")
            return
        queue = [self.root]
        while queue:
            temp = queue.pop(0)
            print(temp.data, end=" ")

            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        print()

if __name__ == "__main__":
    tree = BinaryTree()
    for value in [1, 2, 3, 4, 5, 6, 7]:
        tree.insert(value)
    print("Binary Tree Value Inserted .....")
    print("Binary Tree (Level Order):")
    tree.print_tree()
