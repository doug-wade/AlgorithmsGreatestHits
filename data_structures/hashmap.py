import collections

def flatten_keys(to_flatten):
    for elem in to_flatten:
        if isinstance(elem, list) and not isinstance(elem, str):
            for subelem in flatten_keys(elem):
                yield subelem
        else:
            yield elem[0]

class HashMap:
    """
    Initializes the hashmap with a size of size.
    """
    def __init__(self, size):
        self.array = [None] * size
        # Cache the size rather than checking len every time.
        self.size = size

    """
    Remove all keys from the hashmap
    """
    def clear(self):
        for i in range(0, self.size):
            self.array[i] = None

    """
    Add a key-value pair to the hashmap
    """
    def put(self, key, value):
        index = key.hash % self.size
        if isinstance(self.array[index], list):
            self.array[index].append((key, value))
        elif self.array[index] == None:
            self.array[index] = (key, value)
        else:
            self.array[index] = [self.array[index], (key, value)]

    """
    Add all key-value pairs from a list into the hashmap, in the form
    """
    def putAll(self, key_value_pairs):
        for key_val_pair in key_value_pairs:
            self.put(key_val_pair[0], key_val_pair[1])

    """
    Get a value for a given key, or None if the key does not occur in the hashmap
    """
    def get(self, key):
        index = key.hash % self.size
        if self.array[index] == None:
            return None
        elif isinstance(self.array[index], list):
            return [ v for (k, v) in self.array[index] if k == key ][0]
        else:
            return self.array[index][1]

    """
    Get all keys currently present in the hashmap
    """
    def keys(self):
        return set(flatten_keys([ elem for elem in self.array if elem is not None ]))
