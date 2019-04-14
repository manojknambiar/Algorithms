# LinkedList Implementation
# Author : Manoj Nambiar

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
    def insert(self,element,position=0):
        """   
        first element is considered to be at postion 0

        """
        counter = 0
        if position == 0:
            headElement = self.head
            element.next = headElement
            self.head = element
        else:
            current = self.head
            while current.next:
                if counter == (position - 1):
                    element.next = current.next
                    current.next = element
                current = current.next
                counter += 1

    def delete(self,value):
        """
        deletes only the fist match

        """
        current = self.head
        if current.value == value: # if the element is the header
            self.head = current.next
        else:
            while current.next:
                if current.next.value == value:
                    current.next = current.next.next
                    break
                current = current.next

def main():

    n = node(10)
    k = node(20)
    j = node(30)
    m = node(40)
    a = node(50)

    l1 = linkedlist(n)
    l1.append(k)
    l1.append(j)
    #l1.display()
    #print(l1.search(40))
    l1.insert(m)
    #l1.display()
    l1.insert(a,position=2)
    #l1.display()
    l1.delete(10)
    l1.delete(40)
    l1.display()

if __name__ == "__main__":
    main()

