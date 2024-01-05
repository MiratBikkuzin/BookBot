LEXICON_RU: dict[str, str] = {
    'forward': '>>',
    'backward': '<<',
    '/start': '<b>Привет, %s!</b>\n\nЭто бот, в котором '
              'ты можешь прочитать книгу Бодо Шефера "Путь к финансовой '
              'независимости"\n\nЧтобы посмотреть список доступных '
              'команд - набери /help',
    'reset_start': '<b>Привет снова, %s!</b>\n\nТы уже знаешь, что '
                   'этот бот делает поэтому <b>не нажимай команду '
                   '/start много раз</b>',
    '/help': '<b>Это бот-читалка</b>\n\nДоступные команды:\n\n/beginning - '
             'перейти в начало книги\n/continue - продолжить '
             'чтение\n/bookmarks - посмотреть список закладок\n/help - '
             'справка по работе бота\n\nЧтобы сохранить закладку - '
             'нажмите на кнопку с номером страницы\n\n<b>Приятного чтения!</b>',
    '/bookmarks': '<b>Это список ваших закладок:</b>\n\n'
                  'Нажмите на закладку, чтобы посмотреть её содержимое',
    '/update': '<b>Приветствую, администратор.</b>\n\n'
               'Чтобы добавить книгу в общий доступ отправьте название книги',
    'other_update_command': '<b>Вы не администратор</b>\n'
                            'Данная команда вам недоступна',
    'edit_bookmarks': '<b>Редактировать закладки</b>\n\n'
                      'Нажмите на закладку, чтобы её удалить',
    'edit_bookmarks_button': '❌ РЕДАКТИРОВАТЬ',
    'del': '❌',
    'cancel': 'ОТМЕНИТЬ',
    'back_bookmark_button': 'Вернуться назад',
    'no_bookmarks': 'У вас пока нет ни одной закладки.\n\nЧтобы '
                    'добавить страницу в закладки - во время чтения '
                    'книги нажмите на кнопку с номером этой '
                    'страницы\n\n/continue - продолжить чтение',
    'cancel_text': '/continue - продолжить чтение',
    'other_text': 'Извините, но я не понимаю команду <b>%s</b>. '
                  'Пожалуйста, попробуйте еще раз или воспользуйтесь '
                  'командой <b>/help</b> для получения дополнительной '
                  'информации о доступных командах'
}

LEXICON_COMMANDS_RU: dict[str, str] = {
    '/beginning': 'В начало книги',
    '/continue': 'Продолжить чтение',
    '/bookmarks': 'Мои закладки',
    '/help': 'Справка по работе бота',
    '/update': 'Команда для администраторов'
}