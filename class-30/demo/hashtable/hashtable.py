from linked_list import LinkedList

class Hashtable:

    def __init__(self, size=1024):
        self.size = size
        self._buckets = size * [None]

    def _hash(self, key):
        # Will need to factor HT len
        # Max index is HT len -1
        # >= 0
        # abc
        # a = 97
        # b = 98
        # c = 99
        # sum = 294

        sum = 0
        
        for ch in key:
            sum += ord(ch)
        
        primed = sum * 19

        index = primed % self.size

        return index


    def set(self, key, value):
        pass
        # Hash The key
        hashed_key_index = self._hash(key)

        # Determine if the bucket is empty
        # if it is empty create ll, otherwise add to the ll
        if not self._buckets[hashed_key_index]:
            self._buckets[hashed_key_index] = LinkedList()
        
        self._buckets[hashed_key_index].add((key, value))

    def get(self, requested_key):
        pass
        # Run our requested_key through the _hash method

        # assign the bucket to temp variable with the hashed index

        # check if the index is empty or not
        
        # assign something to the head of the linked list 'current'

        # (key, value) this is going to be the value of each LL
        # current.data[0] = key
        # current.date[1] = value

        # does my key in the linked_list = requesting_key
        # return the value

        # current = current.next

    def contains(self):
        pass