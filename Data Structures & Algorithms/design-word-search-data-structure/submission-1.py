class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.word = True

    def search(self, word: str) -> bool:
        # .に対応するため、DFSを使う
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                # .だった場合、すべてのchildren(value)を検証する
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i+1, child):
                            return True

                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]

            return cur.word

        return dfs(0, self.root)
        
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False