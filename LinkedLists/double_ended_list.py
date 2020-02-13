"""
double_ended_list.py
~~~~~~~~~~~~~~~~~~~
"""

class Node(object):

    def __init__(self, data: int):
        self.data: int = data
        self.next: Node = None


class DoubleEndedList(object):
    """Double Ended List Data Structure"""

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
            self.head = new_node

    def insert_back(self, data: int):
        """Insertion from the end of the list"""
        new_node = Node(data=data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def delete_front(self):
        """Delete the first element of the list"""
        if self.head:
            deleted = self.head
            self.head = self.head.next
            return deleted

    def delete_back(self):
        """Delete the last element of the list"""
        if self.head:
            current = self.head
            previous = self.head
            while current:
                if not current.next:
                    deleted = current
                    self.tail = previous
                    previous.next = None
                    return deleted
                else:
                    previous = current
                    current = current.next
    
    def insert_between(self, data: int, left: int):
        """Insert between two nodes"""
        if self.head and self.head.next:
            current = self.head
            previous = self.head
            while current:
                if current.data == left:
                    new_node = Node(data=data)
                    previous = current
                    current = current.next
                    previous.next = new_node
                    new_node.next = current
                if current.data != left and current.next:
                    previous = current
                    current = current.next
                if not current.next:
                    return None
    
    def delete_between(self, data: int):
        """Delete an element between nodes"""
        if self.head:
            current = self.head
            previous = self.head
            while current:
                if self.head.data == data:
                    deleted = self.head
                    self.head = self.head.next
                    return deleted
                if current.data != data and current.next is not None:
                    previous = current
                    current = current.next
                if current.data == data:
                    deleted = current
                    previous.next = current.next
                    return deleted
                if not current.next:
                    return None
                
    def search(self, data: int):
        """Search for a specified element in the list"""
        current = self.head
        while current:
            if self.head.data == data:
                return self.head
            if current.data == data:
                return current
            if not current.next:
                return None
            else:
                current = current.next

    def print_list(self):
        """Print out the elements of the linked list"""
        current = self.head
        while current:
            print(f"[{current} | {current.data}]")
            current = current.next

def main():
    double_ended_list = DoubleEndedList()
    double_ended_list.insert_front(data=0)
    double_ended_list.insert_front(data=1)
    double_ended_list.insert_front(data=2)
    double_ended_list.insert_back(data=4)
    double_ended_list.delete_front()
    double_ended_list.print_list()
    print(double_ended_list.tail.data)
    double_ended_list.delete_back()
    double_ended_list.print_list()
if __name__ == '__main__':
    main()
