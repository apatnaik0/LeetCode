import bisect
class Router:

    def __init__(self, memoryLimit: int):
        self.q = deque()
        self.cap = memoryLimit
        self.dest_map = defaultdict(list)
        self.p_set = set()

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source,destination,timestamp)
        if packet in self.p_set:
            return False
        self.p_set.add(packet)
        self.q.append(packet)
        self.dest_map[packet[1]].append(packet[2])
        if len(self.q)>self.cap:
            old = self.q.popleft()
            self.dest_map[old[1]].pop(0)
            self.p_set.remove(old)
        return True
        
    def forwardPacket(self) -> List[int]:
        if len(self.q)==0:
            return []
        packet = self.q.popleft()
        self.dest_map[packet[1]].pop(0)
        self.p_set.remove(packet)
        return list(packet)

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        packets = self.dest_map[destination]
        # return self.bsright(packets,endTime) - self.bsleft(packets,startTime)
        return bisect.bisect_right(packets,endTime)-bisect.bisect_left(packets,startTime)

    def bsleft(self, arr, time):
        low = 0
        high = len(arr)-1
        while low<=high:
            mid = (low+high)//2
            if arr[mid][2] >= time:
                high = mid-1
            else:
                low = mid+1
        return low
    
    def bsright(self, arr, time):
        low = 0
        high = len(arr)-1
        while low<=high:
            mid = (low+high)//2
            if arr[mid][2] <= time:
                low = mid+1
            else:
                high = mid-1
        return low


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)