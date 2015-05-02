class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = []

    def __contains(self, to_check, array):
        return len([ elem.letter for elem in array if elem.letter == to_check ]) > 0

    def __get_child_node(self, to_get, array):
        child_nodes = [ elem for elem in array if elem.letter == to_get ]
        if len(child_nodes) == 0:
            to_add = TrieNode(to_get)
            array.append(to_add)
            return to_add
        else:
            return child_nodes[0]

    def find(self, to_find):
        if self.__contains(to_find[0], self.children):
            if len(to_find) > 1:
                return self.__get_child_node(to_find[0], self.children).find(to_find[1:len(to_find)])
            else:
                return True
        else:
            return False

    def add_string(self, to_add):
        if to_add is "":
            return

        if self.__contains(to_add[0], self.children):
            child_node = self.__get_child_node(to_add[0], self.children)
        else:
            child_node = TrieNode(to_add[0])
            self.children.append(child_node)

        child_node.add_string(to_add[1:len(to_add)])

    def to_string(self, prefix):
        to_return = ""
        prefix += self.letter
        if len(self.children) == 0:
            return prefix
        for child in self.children:
            if to_return == "":
                to_return = child.to_string(prefix)
            else:
                to_return += "; " + child.to_string(prefix)
        return to_return

class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def find(self, to_find):
        return self.root.find(to_find)

    def add_string(self, to_add):
        self.root.add_string(to_add)

    def __str__(self):
        return self.root.to_string("")
