class Node:

    """"
    An object for storing a single node of a linked list

    Models two attributes, data and the link to the next node in the list"""
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data


class linked_list:
    """
    Singly linked list
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        return (self.head == None)

    def size(self):
        """returns the number of nodes in the lsit

        takes 0(n) time
        """
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        """
    adds a new node containg data at the head of the list
    takes o(n)"""
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
               return current
            else:
               current = current.next_node 
        return None
        
    def __repr__(self):
        """Returns a string representation of the list
        takes O(n) time
        """
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append(f"[Head: {current.data}]")
            elif current.next_node is None:
                nodes.append(f"[Tail: {current.data}]")
            else:
                nodes.append(f"[{current.data}]")
            current = current.next_node
        return'-> '.join(nodes)