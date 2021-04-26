from data_classes.linked_list import LinkedList

class HashTable:

    def __init__(self, size=256):
        self._size = size
        self._bucket = self._size * [LinkedList()]


    def __str__(self):
        return f'hashtable instance, size: {self._size}'


    def __repr__(self):
        return f'{self.__records__()} entries found in HashTable'

    
    def __records__(self):
        entries = 0
        for el in self._bucket:
            if el.__len__() == 0:
                continue
            else:
                entries += int(el.__len__())
        return entries
    

    def _hash(self, key):
        sum = 0

        for char in key:
            sum += ord(char)

        primed = sum * 23

        return primed % self._size


    def add(self, key, value):
        if self.contains(key):
            raise KeyError(f'hashtable already contains key: {key} at the hashable index')

        else:
            self._bucket[self._hash(key)].insert((key, value))
        
            

    def contains(self, key):
        bucket = self._bucket[self._hash(key)]
        curr = bucket.head

        if not curr:
            return False
        
        while curr:
            if curr.value[0] == key:
                return True
            else:
                curr = curr.next 
        
        return False

