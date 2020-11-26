class LinkedListIterator:
    """This is creating an iter using the __iter__
    largely taken from https://stackoverflow.com/questions/50032481/linked-list-iterator-python
    https://thispointer.com/python-how-to-make-a-class-iterable-create-iterator-class-for-it/
    """
    def __init__(self, head):
        self.current = head
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            item = self.current.data
            self.current = self.current.next
            return item

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
    def __str__(self):
        return f"{self.data}"

class singly_linked_list:

    def __init__(self):
        self.tail = Node(None)
        self.head = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.count = 0
    
    def __repr__(self):
        out = '['
        if self.head.next != self.tail:             
            cur = self.head.next.next
            out = out + str(self.head.next.data)
            while cur != self.tail:
                out = out + ' -> ' + str(cur.data)
                cur = cur.next
        out = out + ']'
        return out
    
    def __iter__(self):
        return LinkedListIterator(self.head)

    
    def iterate_item(self):
        # Iterate the list.
        #This will not include the null values in the head and tail sentinel
        current_item = self.head.next
        while current_item != self.tail:
            val = current_item.data
            current_item = current_item.next
            yield val
            


    def append_item(self, data):
        n = Node(data)
        if self.head.next == self.tail:
            n.next = self.tail
            n.prev = self.head
            self.tail.prev = n
            self.head.next = n
            self.count += 1
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            
            n.next = self.tail
            n.prev = current
            current.next = n
            self.count += 1


#test the repr of Node
n1 = Node("COBOL")
print(n1)

#create items from string in class and also from node class
items = singly_linked_list()
items.append_item('PHP')
items.append_item('Python')
items.append_item('C#')
items.append_item('C++')
items.append_item('Java')
items.append_item(n1)



#test the repr of linkedlist
print(items)

#test the iterate method
for val in items.iterate_item():
    print(val)


#test the count variable
print(items.count)

#test the __iter__ clas and method
for item in items:
    print(item)
