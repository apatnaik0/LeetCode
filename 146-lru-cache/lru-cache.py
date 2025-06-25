class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def delete(self,node):
        front = node.next
        prev = node.prev
        prev.next = front
        front.prev = prev

    def add(self,node):
        front = self.head.next
        self.head.next = node
        node.next = front
        node.prev = self.head
        front.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            ans = self.cache[key].val
            self.delete(self.cache[key])
            self.add(self.cache[key])
            return ans
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(self.cache[key])
        self.cache[key] = Node(key,value)
        self.add(self.cache[key])
        if len(self.cache)>self.capacity:
            lru = self.tail.prev
            self.delete(lru)
            del self.cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)