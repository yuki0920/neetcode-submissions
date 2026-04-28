class CountSquares:

    def __init__(self):
        # tupleで個数を保持する
        self.point_count = defaultdict(int)
        self.points = set()

    def add(self, point: List[int]) -> None:
        self.point_count[tuple(point)] += 1
        self.points.add(tuple(point))
        

    def count(self, point: List[int]) -> int:
        # 始点
        px, py = point
        
        ans = 0
        # 対角線上の点を探し、見つかったら、その両辺の点の個数を追加する(なければ0が追加される)
        for x, y in self.points:
            if abs(px - x) != abs(py - y):
                continue
            if px == x or py == y:
                continue

            # 対角線上の点以外の2つの点は、(x, py), (px, y)
            ans += self.point_count[(x, y)] * self.point_count[(x, py)] * self.point_count[(px, y)]

        return ans
            

            
        
