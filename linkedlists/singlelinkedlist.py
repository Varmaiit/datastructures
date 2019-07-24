# Implementation of linked list in python
# Ref: https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python/


class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_date(self):
        return self.data

    def get_next(self):
        return self.next_node
    
    def set_next(self, new_next):
        self.next_node = new_next
        
    
class LinkedList(object):

    def __init__(self, head=None):
        self.head = head


    def insert(self, data):
        """ Creates a new node with the data and adds it at the head """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node

    def traverse(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next_node

    def delete(self, position):
        
        # if linked list is empty
        if self.head == None:
            return

        temp = self.head

        if position == 0:
            self.head = temp.next_node
            temp = None
            return
        
        # If node needs to be deleted
        for i in range(position-1):
            temp = temp.next_node
            if temp is None:
                break
        
        # if position is more than lenth of l list
        if temp is None or temp.next_node is None:
            return

        """ temp is previous node
            temp.next is to be deleted node 
            temp.next.next is hte next """

        previous_node = temp
        next_node = temp.next_node.next_node

        temp.next_node =None
        previous_node.next_node =next_node




        


        

    
if __name__=='__main__': 
    "Code execution......"
    llist = LinkedList()
    llist.insert(3)
    llist.insert(4)
    llist.insert(9)
    llist.insert(34)
    print("printing the linked list")
    llist.traverse()
    print("deleting the node at position 2")
    llist.delete(2)
    print("printing the new linked list")
    llist.traverse()




    