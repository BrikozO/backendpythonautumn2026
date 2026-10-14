from lesson5 import Book, Groups, add_contact, ask, find_contact, list_contacts, show_group


def main() -> None:
    book: Book = {}
    groups: Groups = {'друзья': set(), 'работа': set(), 'семья': set()}

    while True:
        cmd = ask('Команда: ').lower()
        if cmd == 'выход':
            break
        elif cmd == 'добавить':
            add_contact(book, groups)
        elif cmd == 'найти':
            card = find_contact(book, ask('Имя: '))
            print(card or 'Нет такого контакта')
        elif cmd == 'группа':
            show_group(book, groups, ask('Группа: '))
        elif cmd == 'список':
            list_contacts(book)


main()
