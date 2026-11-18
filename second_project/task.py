import json
from abc import ABC, abstractmethod

from second_project.domain.tasks import Task
from second_project.domain.tasks_list import TaskList


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
