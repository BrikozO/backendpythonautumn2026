book = {}
groups = {"друзья": set(), "работа": set(), "семья": set()}

while True:
    cmd = input("Команда: ").strip().lower()
    if cmd == "выход":
        break
    elif cmd == "добавить":
        name = input("Имя: ").strip()

        if not 2 <= len(name) <= 30:
            print('Имя: от 2 до 30 символов')
            continue

        if name in book:
            print(f'Контакт {name} уже есть в записной книжке')
            continue

        phone = input('Телефон: ').strip()
        ok = phone.startswith('+7') and len(phone) == 12

        for ch in phone[2:]:
            if not ch.isdigit():
                ok = False
                break

        if not ok:
            print('Формат: +7XXXXXXXXXX')
            continue

        email = input('Email: ').strip()

        if '@' not in email:
            print('Email должен содержать @')
            continue

        print('Группы:', ', '.join(groups))
        chosen = input('Группы через запятую (Enter - без группы): ').strip().lower()
        chosen = {g.strip() for g in chosen.split(',') if g.strip()}
        unknown = chosen - set(groups)

        if unknown:
            print('Нет таких групп:', ', '.join(unknown))
            continue

        book[name] = {"phone": phone, "email": email}
        for g in chosen:
            groups[g].add(name)
        print(f'Имя {name} добавлено в записную книжку')
    elif cmd == "список":
        print('Всего контактов', len(book))
        for i, (name, contact) in enumerate(book.items(), 1):
            print(f'{i}. {name}. {contact["phone"]}. {contact["email"]}')
    elif cmd == "найти":
        query = input('Введите подстроку по которой хотите выполнить поиск: ').strip().lower()
        is_any_founded = False
        for name, contact in book.items():
            if query in name.lower() or query in contact["phone"] or query in contact["email"].lower():
                print(name, '-', contact["phone"], '-', contact["email"])
                is_any_founded = True
        if not is_any_founded:
            print("Ничего не найдено!")
    elif cmd == "группа":
        group = input(f'Группа ({", ".join(groups)}): ').strip().lower()

        if group not in groups:
            print("Нет такой группы!")
            continue

        print(f'В группе {group}:', len(groups[group]))
        for name in sorted(groups[group]):
            print(name, '-', book[name]["phone"])
    elif cmd == "выборка":
        print("Выборки (введите номер выборки): 1 - по первой букве")
        kind = input("Выборка: ").strip()
        if kind == "1":
            letter = input('Введите букву: ').strip().upper()[:1]
            count = 0
            for name, contact in book.items():
                if name[:1].upper() == letter:
                    print(name, '-', contact["phone"])
                    count += 1
            print('Найдено: ', count)
        else:
            print("Нет такой выборки!")
    else:
        print("Неизвестная команда!")
