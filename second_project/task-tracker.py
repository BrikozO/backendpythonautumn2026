import json

FILE = 'tasks.json'


def load_tasks() -> list[dict]:
    try:
        with open(FILE, encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.decoder.JSONDecodeError:
        print('Файл поврежден и не может быть прочитан!')
        return []


def save_tasks(tasks: list[dict]) -> None:
    with open(FILE, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def add_task(tasks: list[dict], title: str) -> None:
    task_id = len(tasks) + 1
    tasks.append({'id': task_id, 'title': title, 'done': False})
    print(f'Задача #{task_id} добавлена!')


def complete_task(tasks: list[dict], task_id: int) -> None:
    try:
        task = next(task for task in tasks if task['id'] == task_id)
        task['done'] = True
        print(f'Задача #{task_id} выполнена!')
        return
    except StopIteration:
        print('Задачи #task_id нет')


def show_tasks(tasks: list[dict]) -> None:
    if not tasks:
        print('Список задач пока пуст!')
    for task in tasks:
        mark = 'x' if task['done'] else ' '
        print(f'{task["id"]}. [{mark}] {task["title"]}')


def main():
    tasks = load_tasks()
    print('Комманды: add, done, list, exit')
    while True:
        command, _, arg = input('> ').partition(' ')
        if command == 'add':
            add_task(tasks, arg)
        elif command == 'done':
            try:
                complete_task(tasks, int(arg))
            except ValueError:
                print('Номер задачи должен быть целым числом')
        elif command == 'list':
            show_tasks(tasks)
        elif command == 'exit':
            break
        save_tasks(tasks)

main()