class Task:
    def __init__(self, task_id: int, title: str, done: bool = False):
        self.task_id = task_id
        self.title = title
        self._done = done

    def complete(self) -> None:
        self._done = True

    def __str__(self) -> str:
        mark = 'x' if self._done else ' '
        return f'{self.task_id}. [{mark}] {self.title}'


class TaskList:
    def __init__(self, tasks: list[Task] | None = None):
        self._tasks = tasks or list()

    def add(self, title: str) -> Task:
        task = Task(len(self._tasks) + 1, title)
        self._tasks.append(task)
        return task

    def get(self, task_id: int) -> Task | None:
        for task in self._tasks:
            if task.task_id == task_id:
                return task
        return None

    def __len__(self) -> int:
        return len(self._tasks)

    def __iter__(self):
        return iter(self._tasks)


tasks = TaskList()

tasks.add('Задача 1')
tasks.add('Задача 2')
tasks.get(2).complete()

for task in tasks:
    print(task)
