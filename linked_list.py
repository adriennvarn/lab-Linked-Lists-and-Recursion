class Node:
    """
    A Node class to store integer data and a reference to the next node.
    """

    def __init__(self, data):
        """
        TODO:
        - Assign the provided 'data' to an instance variable.
        - Initialize 'next' to None.
        """
        self.data = data
        self.next = None


class LinkedList:
    """
    A singly linked list that holds Node objects and performs operations using recursion.
    """

    def __init__(self):
        """
        TODO:
        - Initialize 'head' to None to represent an empty list.
        """
        self.head = None

    def insert_at_front(self, data):
        """
        TODO:
        - Create a new Node with 'data'.
        - Insert it at the front of the list (head).
        - Update 'head' to the new node.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """
        (Optional) TODO:
        - Create a new Node with 'data'.
        - Traverse to the end of the list.
        - Set the last node's 'next' reference to the new node.
        """
        new_node = Node(data)
        current = self.head
        if not current:
            self.head = new_node
            return
        
        while current.next:
            current = current.next
        current.next = new_node
            

    def recursive_sum(self):
        """
        TODO:
        - Use recursion to sum all node data in the list.
        - Consider a helper function that:
          1. Checks if the current node is None, and returns 0 if so.
          2. Otherwise, returns node.data + recursive call on node.next.
        - Return the total sum.
        """
        def return_data(node):
            if not node:
                return 0
            return node.data + return_data(node.next)
        
        return return_data(self.head)

    def recursive_reverse(self):
        """
        TODO:
        - Reverse the list in-place using recursion.
        - Possible approach:
          1. Use a helper function that accepts 'prev' and 'current'.
          2. Base case: if current is None, return 'prev' (new head).
          3. Otherwise, swap pointers and recurse.
        - Update 'head' to the returned new head.
        """
        def reverse_list(current, prev):
            if not current:
                return prev
            
            next_node = current.next
            current.next = prev
            
            return reverse_list(next_node, current)
        
        self.head = reverse_list(self.head, None)
        

    def recursive_search(self, target):
        """
        TODO:
        - Return True if 'target' is found, otherwise False, using recursion.
        - Consider a helper function that:
          1. Returns False if the current node is None.
          2. Returns True if current node's data == target.
          3. Otherwise, recurse on the next node.
        """
        pass

    def display(self):
        """
        TODO:
        - Print the contents of the list for debugging.
        - Traverse from 'head' and collect each node's data.
        - Format output as 'val -> val -> val -> None' or similar.
        """
        pass
