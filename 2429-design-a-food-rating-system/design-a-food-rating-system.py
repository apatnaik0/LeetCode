class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_to_cuisine = defaultdict()
        self.cuisine_pq = defaultdict(list)
        for f,c,r in zip(foods,cuisines,ratings):
            self.food_to_cuisine[f] = (c,r)
            heappush(self.cuisine_pq[c],(-r,f))
        
    def changeRating(self, food: str, newRating: int) -> None:
        heappush(self.cuisine_pq[self.food_to_cuisine[food][0]],(-newRating,food))
        self.food_to_cuisine[food] = (self.food_to_cuisine[food][0],newRating)

    def highestRated(self, cuisine: str) -> str:
        for i in range(len(self.cuisine_pq[cuisine])):
            rating,food = self.cuisine_pq[cuisine][0]
            if -rating == self.food_to_cuisine[food][1]:
                return food
            heappop(self.cuisine_pq[cuisine])


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)