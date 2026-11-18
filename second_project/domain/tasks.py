from typing import Self


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

    def to_dict(self) -> dict:
        return {'task_id': self.task_id, 'title': self.title, 'done': self._done}

    @classmethod
    def from_dict(cls, data: dict) -> Self:
        return cls(data['task_id'], data['title'], data['done'])
