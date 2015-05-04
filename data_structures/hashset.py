from hashlib import md5

class HashSet:
    """
    An implementation of a hash set.  Supports strings, ints, and any class that implements __hash__.
    Note that all sets contain None.
    """
    def __init__(self):
        self.array = [None] * 8
        self.__size = 0

    def add(self, elem):
        """
        Add an element to the set.
        """
        if self.array[self.__find_pos(elem)] != elem:
            self.array[self.__find_pos(elem)] = elem
            self.__size += 1
            if self.__size > (len(self.array) / 2):
                self.__rehash()

    def add_all(self, elems):
        """
        Add all elements from an iterable to the set.
        """
        for elem in elems:
            self.add(elem)

    def contains(self, elem):
        """
        Returns true if the element is in the set, false otherwise.  All sets are considered to contain None.
        """
        return elem is None or self.array[self.__find_pos(elem)] is not None

    def size(self):
        """
        Returns the number of elements currently in the set.
        """
        return self.__size

    def __find_pos(self, elem):
        """
        An internal method for determining the position for an element in the backing list.
        """
        if elem is None:
            return 0

        offset = 1

        if isinstance(elem, int):
            position = elem % len(self.array)
        elif isinstance(elem, str):
            digest = md5(elem.encode('utf-8')).hexdigest()
            position = int(digest, 16) % len(self.array)
        else:
            # Throws an AttributeError if hash isn't implemented, which seems reasonable
            position = elem.hash % len(self.array)

        while self.array[position] is not None:
            if (self.array[position] == elem):
                break
            else:
                position += offset
                offset += 1
                while position >= len(self.array):
                    position -= len(self.array)

        return position

    def __rehash(self):
        """
        An internal method for resizing the backing list.
        """
        old_elems = self.array
        self.array = [None] * (len(old_elems)**2)
        self.__size = 0
        self.add_all(old_elems)
