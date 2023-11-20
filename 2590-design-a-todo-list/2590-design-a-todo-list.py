from collections import defaultdict
from sortedcontainers import SortedList as BST
class TodoList:

    def __init__(self):
        self.counter = 0
        self.users_tasks = defaultdict(BST)
        self.complete = defaultdict(set)
        self.user_tags = defaultdict(set)

    def addTask(self, userId: int, taskDescription: str, dueDate: int, tags: List[str]) -> int:
        self.counter += 1
        task_id = self.counter

        self.users_tasks[userId].add((dueDate, task_id, taskDescription))
        for tag in tags:
            self.user_tags[(userId, tag)].add((dueDate, taskDescription, task_id))

        return task_id

    def getAllTasks(self, userId: int) -> List[str]:
        # return [desc for _, t, desc in self.users_tasks[userId] if t not in self.complete[userId]]
        res = []
        for _, t, desc in self.users_tasks[userId]:
            if t not in self.complete[userId]:
                res.append(desc)
        return res
        
    def getTasksForTag(self, userId: int, tag: str) -> List[str]:
        result = sorted([(date, desc) for date, desc, task in self.user_tags[(userId, tag)] if task not in self.complete[userId]])
        return map(lambda x: x[1], result)

    def completeTask(self, userId: int, taskId: int) -> None:
        self.complete[userId].add(taskId)