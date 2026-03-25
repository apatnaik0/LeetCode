class Node:
    def __init__(self,key = 0, val = 0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.cap = capacity
        self.cache = {}
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self,node):
        front = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = front
        front.prev = node
        return

    def delete(self,node):
        front = node.next
        back = node.prev
        back.next = front
        front.prev = back
        return

    def get(self, key: int) -> int:
        if key in self.cache:
            self.delete(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(self.cache[key])
        new_node = Node(key,value)
        self.cache[key] = new_node

        if len(self.cache) > self.cap:
            lru = self.tail.prev
            self.delete(lru)
            del self.cache[lru.key]
        
        self.add(self.cache[key])
        return
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)