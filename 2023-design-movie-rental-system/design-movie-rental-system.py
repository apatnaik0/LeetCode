class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.movies = defaultdict(list)
        self.shopmovie = defaultdict(list)
        self.rents = set()
        for s,m,p in entries:
            self.shopmovie[(s,m)] = p
            self.movies[m].append((p,s))
        
        for m in self.movies:
            self.movies[m].sort()

    def search(self, movie: int) -> List[int]:
        ans = []
        for p,s in self.movies[movie]:
            if (s,movie) not in self.rents:
                ans.append(s)
            if len(ans)==5:
                break
        return ans

    def rent(self, shop: int, movie: int) -> None:
        self.rents.add((shop,movie))

    def drop(self, shop: int, movie: int) -> None:
        self.rents.discard((shop,movie))

    def report(self) -> List[List[int]]:
        res = []
        for s,m in self.rents:
            price = self.shopmovie[(s,m)]
            res.append((price,s,m))
        
        res.sort()
        return [[s,m] for p,s,m in res[0:5]]




# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()