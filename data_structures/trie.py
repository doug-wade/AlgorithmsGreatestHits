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

    def __get_next_nonduplicate(self, string):
        if len(string) == 1:
            return string[0]

        for i in range(len(string)):
            if string[i] != string[i+1] and not (self.__is_vowel(string[i]) and self.__is_vowel(string[i+1])):
                return string[i]

    def __is_vowel(self, letter):
        return letter in self.vowels

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
        possibilities = to_find[0]
        possibilities += self.__get_next_nonduplicate(to_find)
        matches = self.__fuzzy_contains(possibilities, self.children)

        if len(matches) < 1:
            return [ "NO SUGGESTION" ]

        acc += self.letter

        if len(to_find) > 1:
            return self.__flatten([ match.fuzzy_find(to_find[1:], acc) for match in matches ])
        else:
            return [ acc + match.letter for match in matches if match.is_word ]

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
