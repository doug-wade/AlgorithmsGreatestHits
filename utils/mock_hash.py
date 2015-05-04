class MockHash:
    def __init__(self, hash, value=None):
        self.hash = hash
        self.value = value or hash

    def __hash__(self):
        return self.hash

    def __eq__(self, other):
        return (isinstance(other, self.__class__) and self.value == other.value)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return "value: " + str(self.value) + "; hash: " + str(self.hash)
