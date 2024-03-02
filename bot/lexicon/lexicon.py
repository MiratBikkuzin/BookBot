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
             'чтение\n/add_book - добавить книгу для чтения\n'
             '/bookmarks - посмотреть список закладок книг\n/top_up - '
             'Пополнить количество для добавления книг\n/help - '
             'справка по работе бота\n\nЧтобы сохранить закладку - '
             'нажмите на кнопку с номером страницы\n\n<b>Приятного чтения!</b>',
    '/add_book': 'Чтобы добавить книгу отправьте файл книги, '
                 'добавив <b>подпись с полным и точным названием этой книги</b> '
                 'при отправке файла\n\nДоступные форматы: <b><i><u>fb2, txt</u></i></b>',
    '/bookmarks': '<b>Выберите книгу закладки которой вы хотите посмотреть</b>',
    '/update': '<b>Приветствую, администратор.</b>\n\n'
               'Чтобы добавить книгу в общий доступ отправьте файл книги, '
               'добавив <b>подпись с полным названием этой книги</b> при отправке файла\n\n'
               'Доступные форматы: <b><i><u>fb2, txt</u></i></b>',
    'other_update_command': '<b>Вы не администратор.</b>\n'
                            'Данная команда вам недоступна',
    'wait_admin_book_download': 'Подождите пока книга грузиться в общий доступ',
    'wait_user_book_download': 'Немного подождите. Книга уже добавляется...',
    'admin_book_download_end': 'Ура! Загрузка книги в общий доступ завершена',
    'user_book_download_end': 'Ура! Книга добавлена и теперь вы в любой момент можете её читать',
    'other_format_send_book': 'Отправлен файл не того формата или не добавлена подпись к файлу',
    'admins_book_in_stock_warning': 'Книга уже есть в общем доступе',
    'users_book_in_stock_warning': 'Вы уже добавляли эту книгу',
    'choice_books_text': 'Выберите откуда вы будете читать',
    'choice_user_books': 'Мои книги',
    'choice_admin_books': 'Книги общего доступа',
    'admin_books_list': 'Здесь расположены книги, которые может прочитать любой пользователь\n'
                        'Выберите книгу, которую вы хотели бы прочитать:',
    'user_books_list': 'Здесь расположены книги, которые вы уже читали или добавили их сами, '
                       'но ещё не читали.\nВыберите книгу, которую вы хотели бы прочитать:',
    'edit_bookmarks': '<b>Редактировать закладки</b>\n\n'
                      'Нажмите на книгу, которую вы хотите редактировать',
    'edit_book_page_marks': 'Нажмите на страницу, которую вы хотите удалить '
                            'из закладок книги',
    'edit_bookmarks_button': '❌ РЕДАКТИРОВАТЬ',
    'del': '❌',
    'cancel': 'ОТМЕНИТЬ',
    'cancel_add_book_end': 'Хорошо, попробуйте добавить книгу в следующий раз.\n\n'
                           'Если у вас что-то не получилось, то напишите в <b>тех.поддержку '
                           '@chitalka_support</b>',
    'back_button': 'Вернуться назад',
    'back_from_bookmarks_list': 'Вернуться к списку книг',
    'no_bookmarks': 'У вас пока нет ни одной закладки.\n\nЧтобы '
                    'добавить страницу в закладки - во время чтения '
                    'книги нажмите на кнопку с номером этой '
                    'страницы\n\n/continue - продолжить чтение',
    'cancel_text': '/continue - продолжить чтение',
    'other_text': 'Извините, но я не понимаю команду <b>%s</b>. '
                  'Пожалуйста, попробуйте еще раз или воспользуйтесь '
                  'командой <b>/help</b> для получения дополнительной '
                  'информации о доступных командах',
    'pay_label': 'Пополнение количества',
    'top_up_quantity_text': 'Выберите количество, которое вы хотите добавить:',
    'ten_books_invoice_title': 'Пополнение количества на 10 добавлений',
    'unlimited_books_invoice_title': 'Пополнение на безлимитное количество добавлений',
    'invoice_description': 'Для добавления на желаемое количество вам нужно будет заплатить.\n'
                           'Если вы готовы, то нажмите на кнопку внизу для оплаты',
    'successful_payment': '<b>Отлично!</b> Вам начислено желаемое количество.\n'
                          'Если возникли какие-то вопросы то смело пишите в тех.поддержку'
                          '<b>@chitalka_support</b>. Также если вы хотите чтобы в читалке '
                          'появились какие-то новые функции, то напишите вашу идею туда же',
    'error_payment_message': 'Вы не можете заплатить за количество добавлений, так как у вас '
                             'безлимитное количество! Платёж отклонён'
}

LEXICON_COMMANDS_RU: dict[str, str] = {
    '/beginning': 'Начать читать',
    '/continue': 'Продолжить чтение',
    '/add_book': 'Добавить книгу для чтения',
    '/bookmarks': 'Мои закладки',
    '/top_up': 'Пополнить количество для добавления книг',
    '/help': 'Справка по работе бота',
    '/update': 'Команда для администраторов'
}