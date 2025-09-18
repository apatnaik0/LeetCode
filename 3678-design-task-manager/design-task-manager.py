class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.task_dict = {}
        self.pq = []
        for u,t,p in tasks:
            heappush(self.pq,(-p,-t,u))
            self.task_dict[t] = (p,u)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_dict[taskId] = (priority,userId)
        heappush(self.pq,(-priority,-taskId,userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId = self.task_dict[taskId][1]
        self.task_dict[taskId] = (newPriority,userId)
        heappush(self.pq,(-newPriority,-taskId,userId))

    def rmv(self, taskId: int) -> None:
        if taskId in self.task_dict:
            del self.task_dict[taskId]

    def execTop(self) -> int:
        while self.pq:
            p,t,u = heappop(self.pq)
            if -t in self.task_dict and (-p,u) == self.task_dict[-t]:
                del self.task_dict[-t]
                return u
        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()