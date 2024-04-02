class DLeftHashTable:
    def __init__(self, entries, buckets_per_entry):
        self.d = entries
        self.buckets_per_entry = buckets_per_entry
        self.table = [[] for _ in range(self.d * self.buckets_per_entry)]

    def hash(self, key, segment):
        return hash(f'{segment}-{key}') % self.buckets_per_entry

    def segment_for_key(self, key):
        return hash(key) % self.d

    def insert(self, key, value):
        segment = self.segment_for_key(key)
        bucket_index = self.hash(key, segment)
        actual_index = segment * self.buckets_per_entry + bucket_index
        for i, (k, v) in enumerate(self.table[actual_index]):
            if k == key:
                self.table[actual_index][i] = (key, value)
                return
        self.table[actual_index].append((key, value))
