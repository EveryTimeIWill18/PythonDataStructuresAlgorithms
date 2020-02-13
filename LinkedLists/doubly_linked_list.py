"""
doubly_linked_list.py
~~~~~~~~~~~~~~~~~~~~~
"""

class Node(object):

    def __init__(self, data: int):
        self.data: int = data
        self.next: Node = None
        self.previous: Node = None


class DoublyLinkedList(object):
    """A Doubly Linked List Data Structure"""

    def __init__(self):
        self.head: Node = None
        self.tail: Node = None


    def insert_front(self, data: int):
        """Insertion from the front of the list"""
        new_node = Node(data=data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
            new_node.previous = self.head

    def insert_back(self, data: int):
        """Insertion at the end of the list"""
        new_node = Node(data=data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def insert_between(self, data: int, left: int):
        """Insertion between two Nodes

        :var left[int]: The Node to the left of where the
        new Node will be inserted.
        """
        if not self.head:
            self.insert_front(data=data)
        elif self.head and not self.head.next:
            self.insert_back(data=data)
        else:
            new_node = Node(data=data)
            current = self.head
            while current:
                if current.data != left and current.next:
                    current = current.next
                elif current.data == left:
                    new_node.next = current.next
                    new_node.previous = current
                    current.next.previous = new_node
                    current.next = new_node
                    return f"Node[{new_node}| {new_node.data}] entered into list"
                elif current.data != left and not current.next:
                    return f"Node with key: {left} not found"

    def delete_front(self):
        """Deletion of the first element of the list"""
        if not self.head:
            return None
        elif self.head and not self.head.next:
            deleted = self.head
            self.head = None
            self.tail = None
            return deleted
        else:
            deleted = self.head
            self.head = self.head.next
            return deleted

    def delete_back(self):
        """Deletion of the last element of the list"""
        if not self.head:
            return None
        elif self.head and not self.head.next:
            deleted = self.tail
            self.head = None
            self.tail = None
            return deleted
        else:
            deleted = self.tail
            self.tail = self.tail.previous
            self.tail.next = None
            return deleted



    def print_list(self):
        """Print out the elements of the linked list"""
        if self.head:
            current = self.head
            while current:
                print(f"[{current} | {current.data}]")
                current = current.next
        else:
            print("List is empty")


def main():
    doubly_linked_list = DoublyLinkedList()
    # doubly_linked_list.insert_front(0)
    # doubly_linked_list.insert_front(-1)
    # doubly_linked_list.insert_front(-2)
    # doubly_linked_list.insert_back(10)
    doubly_linked_list.insert_back(100)
    doubly_linked_list.insert_back(200)
    doubly_linked_list.print_list()
    print("=====================================================")
    # doubly_linked_list.delete_back()
    # doubly_linked_list.delete_back()
    # doubly_linked_list.print_list()
    doubly_linked_list.insert_between(data=150, left=100)
    doubly_linked_list.insert_between(data=175, left=150)
    doubly_linked_list.insert_between(data=190, left=175)
    doubly_linked_list.insert_between(data=125, left=100)
    doubly_linked_list.print_list()

if __name__ == '__main__':
    main()

