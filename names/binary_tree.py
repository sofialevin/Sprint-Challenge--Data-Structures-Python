class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        def find_insert(current_node, value):
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = BinarySearchTree(value)
                    return
                else:
                    return find_insert(current_node.left, value)
            else:
                if current_node.right is None:
                    current_node.right = BinarySearchTree(value)
                    return
                else:
                    return find_insert(current_node.right, value)

        find_insert(self, value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        def search(current_node, target):
            if current_node.value == target:
                return True
            if target < current_node.value:
                if current_node.left is not None:
                    return search(current_node.left, target)
            if target >= current_node.value:
                if current_node.right is not None:
                    return search(current_node.right, target)

            return False

        return search(self, target)