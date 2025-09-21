class SnapshotArray:

    def __init__(self, length: int):
        self.data = [[(0,0)] for _ in range(length)]
        self.snapid = 0

    def set(self, index: int, val: int) -> None:
        if self.data[index][-1][0] == self.snapid:
            self.data[index][-1] = (self.snapid,val)
        else:
            self.data[index].append((self.snapid,val))

    def snap(self) -> int:
        self.snapid += 1
        return self.snapid-1

    def get(self, index: int, snap_id: int) -> int:
        arr = self.data[index]
        i = bisect.bisect_right(arr, (snap_id, float('inf'))) - 1
        return arr[i][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)