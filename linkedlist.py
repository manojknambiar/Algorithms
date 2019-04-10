# LinkedList Implementation


class node(object):
    def __init__(self,value):
        self.value = value
        self.next = None

class linkedlist(object):
    def __init__(self,head=None):
        self.head = head

    def append(self,node):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = node
        else:
            self.head = node

    def display(self):
        current = self.head
        while current.next:
            print(current.value)
            current = current.next
        print(current.value)

    def search(self,searchVal):
        current = self.head
        index = 0
        while current.next:
            if searchVal == current.value:
                return index
            current = current.next
            index += 1
        if searchVal == current.value:
            return index
        else:
            return -1

def main():

    n = node(10)
    k = node(20)
    j = node(30)

    l1 = linkedlist(n)
    l1.append(k)
    l1.append(j)
    l1.display()
    print(l1.search(40))

if __name__ == "__main__":
    main()

