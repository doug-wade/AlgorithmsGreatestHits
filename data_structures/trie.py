import pdb

class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = []
        self.vowels = "aeiou"
        self.is_word = False

    def __contains(self, to_check, array):
        return [ elem for elem in array if elem.letter == to_check ]

    def __contains_vowel(self, string):
        has_vowel = False
        for letter in string:
            has_vowel = has_vowel or self.__is_vowel(letter)
        return has_vowel

    def __flatten(self, list_of_lists):
        return [item for sublist in list_of_lists for item in sublist]

    def __fuzzy_contains(self, to_check, array):
        if self.__contains_vowel(to_check):
            return [ elem for elem in array if self.__is_vowel(elem.letter)]
        else:
            return [ elem for elem in array if elem.letter.lower() in to_check.lower() ]

    def __get_child_node(self, to_get, array):
        child_nodes = [ elem for elem in array if elem.letter == to_get ]
        if len(child_nodes) == 0:
            to_add = TrieNode(to_get)
            array.append(to_add)
            return to_add
        else:
            return child_nodes[0]

    def __get_next_nonduplicate(self, letter, string):
        if len(string) == 1:
            return (string[0], "")

        for i in range(len(string)):
            if letter is not string[i] and not (self.__is_vowel(letter) and self.__is_vowel(string[i])):
                return (string[i], string[i:])

    def __is_vowel(self, letter):
        return letter.lower() in self.vowels

    def find(self, to_find, acc):
        matches = self.__contains(to_find[0], self.children)

        if len(matches) < 1:
            return ""

        acc += self.letter

        if len(to_find) > 1:
            return matches[0].find(to_find[1:], acc)
        elif matches[0].is_word:
            return acc + matches[0].letter
        else:
            return ""

    def fuzzy_find(self, to_find, acc):
        acc += self.letter
        if to_find is "":
            if self.is_word:
                return [ acc ]
            else:
                return []

        matches = []

        if self.letter is not "" and to_find[0] == self.letter:
            possibilities = self.__get_next_nonduplicate(self.letter, to_find)
            pdb.set_trace()
            if possibilities[1] is "" and self.is_word:
                matches.append(acc)
            else:
                for child in self.__fuzzy_contains(possibilities[0], self.children):
                    for match in child.fuzzy_find(possibilities[1], acc):
                        matches.append(match)

        for child in self.__fuzzy_contains(to_find[0], self.children):
            for match in child.fuzzy_find(to_find[1:], acc):
                matches.append(match)

        return matches

    def add_string(self, to_add):
        if to_add is "":
            self.is_word = True
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

    def __str__(self):
        return "letter: " + self.letter + "; children: " + str(self.children)

class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def find(self, to_find):
        return self.root.find(to_find, "")

    def fuzzy_find(self, to_find):
        return self.root.fuzzy_find(to_find, "")

    def add_string(self, to_add):
        self.root.add_string(to_add)

    def __str__(self):
        return self.root.to_string("")
