contacts = []


while True:
    name_or_command = input('Имя (или "стоп" для выхода из цикла или "найти" для поиска): ').strip()
    if name_or_command.lower() == 'стоп':
        break
    elif name_or_command.lower() == 'найти':
        found = []


    if not 2 <= len(name_or_command) <= 30:
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

    # Форматированная строка
    contacts.append([name_or_command, phone])
    print(f'Имя {name_or_command} добавлено в записную книжку')

print('Всего контактов', len(contacts))
for i, contact in enumerate(contacts, 1):
    print(f'{i}. {contact[0]}. {contact[1]}')
