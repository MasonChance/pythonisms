class Node: 
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_

    def __str__(self):
        return f'LinkedList Node, Value: {self.value}'


    def __repr__(self):
        return f'{self.value}'


class LinkedList:
    def __init__(self, head=None, collection=None):
        self.head = head
        if collection:
            for el in reversed(collection):
                self.insert(el)


    def __str__(self):
        return f"Instance of a LinkedList Head has value of {self.head or self.head.value}"


    def __repr__(self):
        return self.head


    def __iter__(self):
        def val_gen():
            curr = self.head
            while curr:
                yield curr.value
                curr = curr.next
        return val_gen()


    def __len__(self):
        return len(list(iter(self)))


    def insert(self, value):
        self.head = Node(value, self.head)


    