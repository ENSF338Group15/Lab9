import random
import string
import matplotlib.pyplot as plt

#1: Generate a list of 1,000,000 random strings
strings = [''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 10))) for _ in range(1000000)]

#2: Generate index values for a table of 1,000 elements, using both hash functions
hash_table_size = 1000
hash_values_0 = [hash(s) % hash_table_size for s in strings]
hash_values_1 = [(hash(s) + 1) % hash_table_size for s in strings]

#3: For each function, generate a plot with index value on the X axis, and #collisions for that value on the Y axis
plt.hist(hash_values_0, bins=hash_table_size, alpha=0.5, label='Hash Function 0')
plt.hist(hash_values_1, bins=hash_table_size, alpha=0.5, label='Hash Function 1')
plt.legend(loc='upper right')
plt.xlabel('Index Value')
plt.ylabel('#Collisions')
plt.show()

# Answer to question 4:
# Observing the plot, though in general, the hash functions exhibit a uniform distribution, there
# are some areas that can be considered "hot spots" where the number of collisions is higher than
# average. These are approximately around index values 100, 340, 380, and 770.