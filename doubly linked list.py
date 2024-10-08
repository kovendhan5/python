# Node of a Doubly Linked List
class Node:
    def __init__(self, data):
        self.data = data  # Data part of the node
        self.prev = None  # Pointer to the previous node
        self.next = None  # Pointer to the next node

# Doubly Linked List
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list as None

    # Insert at the end of the list
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:  # If the list is empty
            self.head = new_node
            return
        last = self.head
        while last.next:  # Traverse to the last node
            last = last.next
        last.next = new_node
        new_node.prev = last

    # Delete a node from the list
    def delete_node(self, key):
        temp = self.head
        
        # If the list is empty
        if temp is None:
            return
        
        # If the node to be deleted is the head node
        if temp is not None and temp.data == key:
            self.head = temp.next  # Change head to the next node
            if self.head:
                self.head.prev = None  # Set the previous of new head to None
            temp = None
            return
        
        # Traverse to find the node to be deleted
        while temp is not None and temp.data != key:
            temp = temp.next

        # Node not found
        if temp is None:
            return
        
        # If the node to be deleted is found
        if temp.next:
            temp.next.prev = temp.prev
        if temp.prev:
            temp.prev.next = temp.next
        temp = None

    # Traverse the list in forward direction
    def traverse_forward(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    # Traverse the list in backward direction
    def traverse_backward(self):
        current = self.head
        if current is None:
            return
        # Go to the last node
        while current.next:
            current = current.next
        # Traverse backward
        while current:
            print(current.data, end=" ")
            current = current.prev
        print()

# Example usage
dll = DoublyLinkedList()
dll.insert_end(10)
dll.insert_end(20)
dll.insert_end(30)
dll.insert_end(40)

print("Traversal in forward direction:")
dll.traverse_forward()

print("Traversal in backward direction:")
dll.traverse_backward()

dll.delete_node(20)
print("After deleting 20:")
dll.traverse_forward()
