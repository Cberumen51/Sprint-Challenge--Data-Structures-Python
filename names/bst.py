class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # take the current value of our node(self.node)
        # compare to the new value we want to insert
        # if there is no node insert root node
        
        # if new value < self.value
            # if self.left is already taken by a node
                # make that node, call insert
            # set the left to the new node with the new value
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
            
        # if new value > self.value
            # if self.right is already taken by a node
                # make that node, call insert
            # set the right to the new node with the new value
        if value > self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

        pass

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        # compare the target to current value
        # if current value < target
        if self.value > target:
            # check the left subtree
            if self.left is None:
                return False
            found = self.left.contains(target)
            # if you cannot go left, return False
        
        # if current value >= target
        if self.value < target:
            # check if right subtree contains target
            # if you cannot go right return False
            if self.right is None:
                return False
            found = self.right.contains(target)
            
        return found
        

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        max_value = self.right.get_max()
        return max_value
        

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(node)
        print(self.value)
        if self.right:
            self.right.in_order_print(node)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # create a queue for nodes
        queue = []
        # add the first node to the queue
        queue.append(node)
        # while queue is not empty
        while len(queue) > 0:
            # remove the first node from the queue
            first_node = queue.pop(0)
            # print the removed node 
            print(first_node.value)
            # add all children into the queue
            if first_node.left:
                queue.append(first_node.left)
            if first_node.right:
                queue.append(first_node.right)
        return queue
        

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # create a stack for nodes
        stack = []
        # add the first node to the stack
        stack.append(node)
        # while the stack is not empty
        while len(stack) > 0:
            # get the current node from the top of the stack
            last_node = stack.pop()
            # print that node
            print(last_node.value)
            # add all children to the stack
            if last_node.left:
                stack.append(last_node.left)
            if last_node.right:
                stack.append(last_node.right)
        return stack
