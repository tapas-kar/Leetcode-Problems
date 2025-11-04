# Design a data structure that supports adding new words and finding if a string matches any previously added string.

# Implement the WordDictionary class:

# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

# Example:

# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]

# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
 

# Constraints:

# 1 <= word.length <= 25
# word in addWord consists of lowercase English letters.
# word in search consist of '.' or lowercase English letters.
# There will be at most 2 dots in word for search queries.
# At most 104 calls will be made to addWord and search.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.endOfWord = True

    def search(self, word: str) -> bool:

        def dfs(j, root):
            curr = root

            # we always want to start this loop at j, whatever it happens to be
            for i in range(j, len(word)):
                c = word[i]

                if c == ".":
                    # when the code is in this block, that means the "." could match any of the 26 characters
                    # not sure if you can do that iteratively, very efficiently
                    # so we are going to use backtracking or recursion to help us do that
                    for child in curr.children.values():
                        # what are we going to pass in the DFS?
                        # we want to know what is the remaining portion of the word that we are trying to find - so we want to pass in the index
                        # another parameter that we want to pass is the context of what is the current node that we are at - that is the child
                        # for the first parameter - it has to be i + 1 because we are going DOWN A CHILD of where the "." is encountered
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]

            # at the end, we want to return if the input word matches any of the words that we have in the Trie
            # if the word exists then return True, otherwise False
            # similar to the search function in Implement Trie Prefix Tree
            return curr.endOfWord
        return dfs(0, self.root)