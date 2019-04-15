# Doubly linked list implementation
# Author : Manoj Nambiar


class node(object):
    def __init__(self,value):
        self.value = value
        self.next = None
        self.previous = None

class doublyLinkedList(object):
    def __init__(self,node=None):
        self.head = node

    def insert(self,node,position=0):
        counter = 0
        if position == 0:
            node.next = self.head
            self.head.previous = node
            self.head = node
        else:
            current = self.head
            while current.next:
                if counter == (position - 1):
                    node.next = current.next
                    node.previous = current
                    current.next = node
                counter += 1
                current = current.next

    def display(self):
        current = self.head
        while current.next:
            print(current.value)
            current = current.next
        print(current.value)

def main():
    a1 = node(10)
    a2 = node(20)
    a3 = node(30)
    a4 = node(40)

    d1 = doublyLinkedList(a1)
    d1.insert(a2,position=0)
    d1.insert(a3,position=1)
    #d1.insert(a4,position=1)
    d1.display()


if __name__ == "__main__":
    main()