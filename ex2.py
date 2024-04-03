import random
import string
import matplotlib.pyplot as plt

# DLeftHashTable class from ex1.py
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

# Initialize DLeftHashTable with size 1000
d_left_hash_table = DLeftHashTable(1000, 1000)

#1: Generate a list of 1,000,000 random strings
strings = [''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 10))) for _ in range(1000000)]

#2: Generate index values for a table of 1,000 elements, using both hash functions
hash_values_0 = [d_left_hash_table.hash(s, 0) for s in strings]  # Use the left hash function (i=0)
hash_values_1 = [d_left_hash_table.hash(s, 1) for s in strings]  # Use the right hash function (i=1)

#3: For each function, generate a plot with index value on the X axis, and #collisions for that value on the Y axis
plt.hist(hash_values_0, bins=1000, alpha=0.5, label='Hash Function 0')
plt.hist(hash_values_1, bins=1000, alpha=0.5, label='Hash Function 1')
plt.legend(loc='upper right')
plt.xlabel('Index Value')
plt.ylabel('#Collisions')
plt.show()

# Answer to question 4:
# Observing the plot, though in general, the hash functions exhibit a uniform distribution, there
# are some areas that can be considered "hot spots" where the number of collisions is higher than
# average. These are approximately around index values 80, 140, and 770.