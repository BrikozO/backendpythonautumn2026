contacts = []


while True:
    cmd = input("Команда: ").strip().lower()
    if cmd == "выход":
        break
    elif cmd == "добавить":
        name = input("Введите имя: ").strip()

        if not 2 <= len(name) <= 30:
            print('Имя: от 2 до 30 символов')
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

        contacts.append([name, phone])
        print(f'Имя {name} добавлено в записную книжку')
    elif cmd == "список":
        print('Всего контактов', len(contacts))
        for i, contact in enumerate(contacts, 1):
            print(f'{i}. {contact[0]}. {contact[1]}')
    elif cmd == "поиск":
        query = input('Введите подстроку по которой хотите выполнить поиск: ').strip().lower()
        is_any_founded = False
        for name, phone in contacts:
            if query in name.lower() or query in phone:
                print(name, '-', phone)
                is_any_founded = True
        if not is_any_founded:
            print("Ничего не найдено!")
    elif cmd == "фильтр":
        print("Фильтры (введите номер фильтра): 1 - по первой букве")
        kind = input("Фильтр:").strip()
        if kind == "1":
            letter = input('Введите букву: ').strip().upper()[:1]
            count = 0
            for name, phone in contacts:
                if name[:1].upper() == letter:
                    print(name, '-', phone)
                    count += 1
            print('Найдено: ', count)
        else:
            print("Нет такого фильтра!")
    else:
        print("Неизвестная команда!")


