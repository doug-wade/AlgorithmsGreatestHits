from hashlib import md5

class HashSet:
    """
    An implementation of a hash set.  Note that all sets contain None.
    """
    def __init__(self):
        self.array = [None] * 8
        self.__size = 0

    def add(self, elem):
        if self.array[self.__find_pos(elem)] != elem:
            self.array[self.__find_pos(elem)] = elem
            self.__size += 1
            if self.__size > (len(self.array) / 2):
                self.__rehash()

    def add_all(self, elems):
        for elem in elems:
            self.add(elem)

    def contains(self, elem):
        return elem is None or self.array[self.__find_pos(elem)] is not None

    def size(self):
        return self.__size

    def __find_pos(self, elem):
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
        old_elems = self.array
        self.array = [None] * (len(old_elems)**2)
        self.__size = 0
        self.add_all(old_elems)
