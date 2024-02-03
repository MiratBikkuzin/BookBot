LEXICON_RU: dict[str, str] = {
    'forward': '>>',
    'backward': '<<',
    '/start': '<b>Привет, %s!</b>\n\nЭто бот, в котором '
              'ты можешь читать книги и добавлять свои'
              '\n\nЧтобы посмотреть список доступных '
              'команд - набери /help',
    'reset_start': '<b>Привет снова, %s!</b>\n\nТы уже знаешь, что '
                   'этот бот делает поэтому <b>не нажимай команду '
                   '/start много раз</b>',
    '/help': '<b>Это бот-читалка</b>\n\nДоступные команды:\n\n/beginning - '
             'начать читать\n/continue - продолжить '
             'чтение\n/bookmarks - посмотреть список закладок книг\n/help - '
             'справка по работе бота\n\nЧтобы сохранить закладку - '
             'нажмите на кнопку с номером страницы\n\n<b>Приятного чтения!</b>',
    '/bookmarks': '<b>Выберите книгу закладки которой вы хотите посмотреть</b>',
    '/update': '<b>Приветствую, администратор.</b>\n\n'
               'Чтобы добавить книгу в общий доступ отправьте файл книги, '
               'добавив <b>подпись с полным названием этой книги</b> при отправке файла\n\n'
               'Доступные форматы: <b><i><u>fb2, txt</u></i></b>',
    'other_update_command': '<b>Вы не администратор.</b>\n'
                            'Данная команда вам недоступна',
    'wait_admin_book_download': 'Подождите пока книга грузиться в общий доступ',
    'admin_book_download_end': 'Ура! Загрузка книги в общий доступ завершена',
    'other_format_admin_send_book': 'Отправлен файл не того формата или не добавлена подпись к файлу',
    'admins_book_in_stock_warning': 'Книга уже есть в общем доступе',
    'choice_books_text': 'Выберите откуда вы будете читать',
    'choice_user_books': 'Мои книги',
    'choice_admin_books': 'Книги общего доступа',
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
    '/beginning': 'Начать читать',
    '/continue': 'Продолжить чтение',
    '/bookmarks': 'Мои закладки',
    '/help': 'Справка по работе бота',
    '/update': 'Команда для администраторов'
}