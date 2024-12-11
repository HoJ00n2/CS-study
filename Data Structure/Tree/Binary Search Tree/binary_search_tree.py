class Tree:
    def __init__(self, value=None):
        # Initialize the Tree node with a value
        self.value = value

        # If the node has a value,
        # create left and right children nodes
        if self.value:
            self.left = Tree()
            self.right = Tree()

        else:
            # If the node has no value,
            # set left and right children to None
            self.left = None
            self.right = None

    # Check if the node is empty (has no value)
    def isempty(self):
        return self.value is None

    # Check if the tree node is a leaf node
    # (both left and right children are None)
    def isleaf(self):
        if self.left.left is None and self.right.right is None:
            return True

        return False

    # Insert a new value into the tre
    def insert(self, data):
        # If the node is empty, insert the data here.
        if self.isempty():
            self.value = data

            # Create left and right children
            # for the inserted node
            self.left = Tree()
            self.right = Tree()
            print(f"{self.value} is inserted successfully.")

        # If data is less than current node value,
        # insert into left subtree
        elif data < self.value:
            self.left.insert(data)
            return

        # If data is greater than current node value,
        # insert into right subtree
        elif data > self.value:
            self.right.insert(data)
            return

        # If data is equal to current node value,
        # do nothing
        elif data == self.value:
            return

    def find(self, v):
        if self.isempty():
            # If the tree is empty, the value is not found
            print(f"{v} is not found")
            return False

        if self.value == v:
            # If the value is found at the current node,
            # print a message and return True
            print(f"{v} is found")
            return True

        if v < self.value:
            # If the value is less than the current node's value,
            # search in the left subtree
            return self.left.find(v)

        else:
            # If the value is greater than the current node's value
            # search in the right subtree
            return self.right.find(v)

    def maxval(self):
        if self.right.right is None:
            return self.value

        return self.right.maxval()

    def delete(self, v):
        if self.isempty():
            return

        if v < self.value:
            self.left.delete(v)
            return

        if v > self.value:
            self.right.delete(v)
            return

        if v == self.value:
            if self.isleaf():
                self.value = None
                self.left = None
                self.right = None
                return

            elif self.left.isempty():
                self.value = self.right.value
                self.left = self.right.left
                self.right = self.right.right
                return

            else:
                self.value = self.left.maxval()
                self.left.delete(self.left.maxval())
                return

    def inorder(self):
        if self.isempty():
            # If the tree is empty, return an empty list
            return []
        else:
            # Return the inorder traversal of the tree
            # (left subtree, root, right subtree)
            return self.left.inorder() + [self.value] + self.right.inorder()
