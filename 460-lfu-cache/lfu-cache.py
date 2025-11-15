class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.freq = 1
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add(self,node):
        front = self.head.next
        node.next = front
        node.prev = self.head
        front.prev = node
        self.head.next = node
        self.size += 1
    
    def delete(self, node):
        front = node.next
        back = node.prev
        front.prev = back
        back.next = front
        self.size -= 1
    
    def del_tail(self):
        tail = self.tail.prev
        self.delete(tail)
        return tail

class LFUCache:

    def __init__(self, capacity: int):
        self.min_freq = 0
        self.cap = capacity
        self.cache = {}
        self.ftable = collections.defaultdict(DLL)

    def get(self, key: int) -> int:
        if key in self.cache:
            return self.update_cache(key, self.cache[key].val)
        else:
            return -1
            
    def put(self, key: int, value: int) -> None:
        if not self.cap:
            return
        if key in self.cache:
            self.update_cache(key,value)
        else:
            if len(self.cache) == self.cap:
                prev_tail = self.ftable[self.min_freq].del_tail()
                del self.cache[prev_tail.key]
            node = Node(key,value)
            self.ftable[1].add(node)
            self.cache[key] = node
            self.min_freq = 1
    
    def update_cache(self, key,value):
        node = self.cache[key]
        node.val = value
        prev_freq = node.freq
        node.freq += 1
        self.ftable[prev_freq].delete(node)
        self.ftable[node.freq].add(node)
        if prev_freq == self.min_freq and self.ftable[prev_freq].size == 0:
            self.min_freq += 1
        return node.val


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)