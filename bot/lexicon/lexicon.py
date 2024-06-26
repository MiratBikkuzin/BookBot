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
             'чтение\n/profile - посмотреть свой профиль\n'
             '/add_book - добавить книгу для чтения\n'
             '/bookmarks - посмотреть список закладок книг\n/top_up - '
             'пополнить количество для добавления книг\n/help - '
             'справка по работе бота\n\nЧтобы сохранить закладку - '
             'нажмите на кнопку с номером страницы\n\n<b>Приятного чтения!</b>\n\n'
             'Оферта: https://docs.google.com/document/d/1MeHm-5O4hU1IyLegMwvGU1P4HEb-3abL/edit?usp=drive_link&ouid=115562507455248513358&rtpof=true&sd=true',
    '/add_book': 'Чтобы добавить книгу для начала отправьте <b>инициалы автора этой книги</b>',
    'book_name_send': 'Теперь отправьте <b>полное и точное название книги</b>',
    'book_file_send': 'Отлично! Теперь отправьте <b>файл книги</b>\n\n'
                      'Доступные форматы: <b><i><u>fb2, pdf, txt</u></i></b>',
    'cancel_add_book_warning': 'Вы уже отменяли добавление книги',
    '/bookmarks': '<b>Выберите книгу закладки которой вы хотите посмотреть</b>',
    '/update': '<b>Приветствую, администратор.</b>\n\n'
               'Выберите, что вы хотите сделать:',
    'other_update_command': '<b>Вы не администратор.</b>\n'
                            'Данная команда вам недоступна',
    'admin_add_book': 'Чтобы добавить книгу в общий доступ для начала отправьте '
                      '<b>инициалы автора этой книги</b>',
    'admin_edit_books': '📚\nНажмите на книгу, чтобы удалить её из общего доступа '
                        '(у пользователей читающих эту книгу удалятся все данные о ней, '
                        'в том числе и её закладки)',
    'admin_add_book_button': 'Добавить книгу',
    'admin_edit_books_button': 'Редактировать книги',
    'admin_del_book_end': 'Книга удалена у всех пользователей вместе с её закладками',
    'wait_admin_book_download': 'Подождите пока книга грузиться в общий доступ',
    'wait_user_book_download': 'Немного подождите. Книга уже добавляется...',
    'add_book_error': '<b>У вас закончилось количество добавлений</b>\n\n'
                      'Сейчас вы не можете добавить книгу.\n'
                      'Выберите количество, которое вы хотите добавить:',
    'add_book_decode_error': 'К сожалению, эту книгу вы не сможете добавить.\n'
                             'Книга содержит <b>старую кодировку</b>, поэтому я '
                             'не могу её загрузить 😔',
    'admin_book_download_end': 'Ура! Загрузка книги в общий доступ завершена',
    'user_book_download_end': 'Ура! Книга добавлена и теперь вы в любой момент можете её читать',
    'other_format_send_book': 'Отправлен файл не того формата',
    'admins_book_in_stock_warning': 'Книга уже есть в общем доступе',
    'users_book_in_stock_warning': 'Вы уже добавляли эту книгу',
    'choice_books_text': 'Выберите откуда вы будете читать',
    'choice_user_books': 'Мои книги',
    'choice_admin_books': 'Книги общего доступа',
    'admin_books_list': 'Здесь расположены книги, которые может прочитать любой пользователь\n'
                        'Выберите книгу, которую вы хотели бы прочитать:',
    'user_books_list': 'Здесь расположены книги, которые вы уже читали или добавили их сами, '
                       'но ещё не читали.\nВыберите книгу, которую вы хотели бы прочитать:',
    'no_books_warning': '<b>У вас нет книг в библиотеке</b>.\n'
                        'Чтобы добавить книгу в библиотеку используйте команду '
                        '/add_book или начните читать книгу с общего доступа',
    'edit_user_books': '📚\n<b>Нажмите на книгу, чтобы удалить её данные</b>\n'
                       'После нажатия книга удалится из вашего списка, '
                       'а также исчезнут все закладки сделанные в этой книге',
    'del_user_book_end': 'Данные о книге "%s" удалены',
    'edit_bookmarks': '🔖\n<b>Редактировать закладки</b>\n'
                      'Нажмите на книгу, закладки которой вы хотите редактировать',
    'edit_book_page_marks': '🔖\nНажмите на страницу, которую вы хотите удалить '
                            'из закладок книги',
    'edit_button': '❌ РЕДАКТИРОВАТЬ',
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
    'add_books_description': '<b>Пополнение количества на %s добавлений</b>\n'
                             'После успешной оплаты нажмите на кнопку проверки платежа\n'
                             'Проверка может занимать определённое время',
    'books_price_button': 'Заплатить %s.00 RUB',
    'check_payment_button': 'Проверить платёж',
    'successful_payment': '<b>Отлично!</b> Вам начислено желаемое количество.\n'
                          'Если возникли какие-то вопросы то смело пишите в тех.поддержку '
                          '<b>@chitalka_support</b>. Также если вы хотите чтобы в читалке '
                          'появились какие-то новые функции, то напишите вашу идею туда же',
    'error_payment_message': 'Вы не оплатили счёт\n'
                             'Если же вы его оплатили, но вы видите это сообщение, '
                             'то это значит, что деньги ещё не дошли на баланс бота.\n'
                             'Попробуйте проверить платёж позже',
    'reverification_error': 'Счёт уже был оплачен и проверка уже была осуществлена'
}

LEXICON_COMMANDS_RU: dict[str, str] = {
    '/beginning': 'Начать читать',
    '/continue': 'Продолжить чтение',
    '/profile': 'Профиль',
    '/add_book': 'Добавить книгу для чтения',
    '/bookmarks': 'Мои закладки',
    '/top_up': 'Пополнить количество для добавления книг',
    '/help': 'Справка по работе бота',
    '/update': 'Команда для администраторов'
}


PROFILE_LEXICON_RU: dict[str, str] = {
    'profile': '📊 <b>Ваш профиль:</b>',
    'name': '👤 <b>Имя:</b>',
    'id': '🖥 <b>ID:</b>',
    'books_started': '📚 <b>Книг в библиотеке:</b>',
    'remaining_additions': '🔢 <b>Добавлений книг осталось:</b>',
    'bookmarks_number': '🔖 <b>Всего закладок:</b>'
}