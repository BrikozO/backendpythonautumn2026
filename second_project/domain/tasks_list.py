from second_project.domain.tasks import Task


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
