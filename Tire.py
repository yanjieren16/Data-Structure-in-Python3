# implementation of trie


class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        # isEndOfWord marks the end of the word.
        self.isEndOfWord = False


class Trie:

    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        return TrieNode()

    # converts key current character into index 
    def _char_to_index(self, ch):
        return ord(ch) - ord('a')

    def insert(self, key):
        
        # if not present, inserts key into tire
        # if key is prefix of tire node, marks leaf node
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._char_to_index(key[level])

            # if current character is not present
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.get_node()
            pCrawl = pCrawl.children[index]

        # mark last node as leaf
        pCrawl.isEndOfWord = True

    def search(self, key):

        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._char_to_index(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]

        return pCrawl is not None and pCrawl.isEndOfWord


def main():

    keys = ["the", "a", "there", "anaswe", "any", "by", "their"]

    output = ["Not present in trie", "Present in tire"]

    t = Trie()

    for key in keys:
        t.insert(key)

    print("{} ---- {}".format("the",output[t.search("the")]))
    print("{} ---- {}".format("these",output[t.search("these")]))
    print("{} ---- {}".format("their",output[t.search("their")]))
    print("{} ---- {}".format("thaw",output[t.search("thaw")]))


if __name__ == '__main__':
    main()

