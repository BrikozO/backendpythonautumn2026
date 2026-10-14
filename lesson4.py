Card = dict[str, str]
Book = dict[str, Card]
Groups = dict[str, set[str]]


def ask(prompt: str) -> str:
    return input(prompt).strip()


def add_contact(book: Book, groups: Groups) -> None:
    name = ask('Имя: ')
    book[name] = {'phone': ask('Телефон: '), 'email': ask('Email: ')}
    for g in ask('Группы: ').split(','):
        g = g.strip().lower()
        if g in groups:
            groups[g].add(name)
        else:
            print('Нет группы', g)


def find_contact(book: Book, name: str) -> Card | None:
    return book.get(name)


def show_group(book: Book, groups: Groups, group: str) -> None:
    for n in groups.get(group, set()):
        if not book[n].get('phone'):
            continue
        print(n, '-', book[n]['phone'])


def list_contacts(book: Book) -> None:
    for name in sorted(book):
        print(name, '-', book[name]['phone'])
