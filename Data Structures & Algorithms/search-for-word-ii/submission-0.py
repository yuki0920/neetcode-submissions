class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # wordsをトライ木に入れる
        # wordsごとに始点を決める
        # 探索済みかどうかを管理するデータ構造を用意する
        # 次の探索箇所が枠内かつ未訪問かつトライ木にあるかを確認する
        # startwithであれば、次へ進む。searchであれば、True。なければ、False

        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


        def dfs(r, c, node, word):
            # 範囲外ならreturn
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return
            # 訪問済みならreturn
            if (r, c) in visit:
                return
            # トライ木の子になければreturn
            char = board[r][c]
            if char not in node.children:
                return

            visit.add((r, c))
            # トライ木を1段下に行く
            node = node.children[char]
            word += char
            # 現在のノードがwordならば、回答に追加する
            if node.isWord:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True