# lexicon/lexicon.py
LEXICON: dict[str, str] = {
    # Приветственное сообщение
    'start': (
        "Привет! Я помогу тебе запоминать дни рождения твоих друзей. "
        "Используй меню ниже или команды для управления.")
    ,
    # Сообщение помощи с описанием всех команд
    'help': (
        "Я бот для хранения дней рождения друзей.\n\n"
        "Доступные команды:\n"
        "/add_birthday - добавить новый день рождения\n"
        "/show_birthdays - показать список всех друзей\n"
        "/today_birthdays - показать, у кого день рождения сегодня\n"
        "/edit_birthday - изменить дату дня рождения друга\n"
        "/delete_birthday - удалить запись о дне рождения\n"
        "/help - показать это справочное сообщение"
    ),
    # Сообщения для диалога добавления нового дня рождения
    'add_name': "Пожалуйста, отправь имя друга, чей день рождения хочешь добавить.",
    'name_exists': "Это имя уже есть в списке! Отправь другое имя.",
    'add_date': "Теперь отправь дату его рождения в формате ДД.MM (день и месяц).",
    'invalid_date': "Неверный формат даты. Попробуй ещё раз в формате ДД.MM:",
    'birthday_added': "Добавлен день рождения: {name} - {date}.",
    # Сообщения для вывода списка дней рождений
    'show_list': "Список дней рождения:",
    'birthday_entry': "{name} - {date}",  # шаблон для строки списка: Имя - дата
    'no_birthdays': "Ты ещё не добавил ни одного дня рождения.",
    # Сообщения для "Дни рождения сегодня"
    'today_list': "Сегодня день рождения у:",
    'no_today': "Сегодня ни у одного из друзей нет дня рождения.",
    # Сообщения для редактирования
    'prompt_edit': "Выбери друга, чей день рождения хочешь изменить:",
    'edit_date': "Введите новую дату для {name} в формате ДД.MM:",
    'birthday_updated': "Обновлена дата рождения: {name} - {date}.",
    # Сообщения для удаления
    'prompt_delete': "Выбери друга, которого хочешь удалить:",
    'birthday_deleted': "Удалён день рождения друга: {name}.",
    # Подписи кнопок (Reply-клавиатура)
    'btn_add': "Добавить день рождения",
    'btn_show': "Показать все дни рождения",
    'btn_today': "Дни рождения сегодня",
    'btn_add_birthday': '➕ Добавить ДР',
    'btn_show_birthdays': '📅 Все ДР',
    'btn_today_birthdays': '🎂 Сегодня',
    'start': 'Привет! Я бот для дней рождения.',
    'help': 'Помощь: ...'

}

