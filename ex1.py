class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, key, value):
        if not self.head:
            self.head = Node(key, value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(key, value)

    def lookup(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def count(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

class DLeftHashTable:
    def __init__(self, entries, buckets):
        self.size = entries
        self.buckets = [LinkedList() for _ in range(buckets)]

    def hash(self, key, i):
        return (hash(key) + i) % self.size

    def insert(self, key, value):
        left_hash = self.hash(key, 0)
        right_hash = self.hash(key, 1)
        if self.buckets[left_hash].count() <= self.buckets[right_hash].count():
            self.buckets[left_hash].insert(key, value)
        else:
            self.buckets[right_hash].insert(key, value)

    def lookup(self, key):
        left_hash = self.hash(key, 0)
        right_hash = self.hash(key, 1)
        left_value = self.buckets[left_hash].lookup(key)
        if left_value is not None:
            return left_value
        else:
            return self.buckets[right_hash].lookup(key)