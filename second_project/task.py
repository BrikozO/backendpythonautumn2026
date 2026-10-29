import json
from abc import ABC, abstractmethod
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


class Storage(ABC):
    @abstractmethod
    def load(self) -> list[Task]:
        pass

    @abstractmethod
    def save(self, tasks: TaskList) -> None:
        pass


class JsonStorage(Storage):
    def __init__(self, path: str):
        self.path = path

    def load(self) -> list[Task]:
        try:
            with open(self.path, encoding='utf-8') as f:
                return [Task.from_dict(t) for t in json.load(f)]
        except FileNotFoundError:
            return []
        except json.decoder.JSONDecodeError:
            print('Файл поврежден и не может быть прочитан!')
            return []

    def save(self, tasks: TaskList) -> None:
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump([t.to_dict() for t in tasks], f, ensure_ascii=False, indent=2)


class App:
    def __init__(self, storage: Storage):
        self.storage = storage
        self.tasks = TaskList(storage.load())

    def run(self) -> None:
        while True:
            command, _, arg = input('> ').partition(' ')
            if command == 'add':
                task = self.tasks.add(arg)
                print(f'Задача #{task.task_id} добавлена!')
            elif command == 'done':
                try:
                    task_id = int(arg)
                except ValueError:
                    print('Номер задачи должен быть целым числом')
                    continue
                task = self.tasks.get(task_id)
                if task is None:
                    print(f'Задачи #{task_id} нет в списке!')
                    continue
                task.complete()
                print(f'Задача #{task_id} выполнена!')
            elif command == 'list':
                if not self.tasks:
                    print('Список задач пуст!')
                    continue
                for task in self.tasks:
                    print(task)
            elif command == 'exit':
                break


if __name__ == '__main__':
    App(JsonStorage('tasks.json')).run()
