add_user_info: str = """
INSERT INTO `users_info` (`user_id`, `page`)
VALUES (%s, %s)"""


update_user_page: str = """
UPDATE `users_info`
SET `page` = %s
WHERE `user_id` = %s"""


user_info_query: str = """
SELECT `user_id`, `page`
FROM `users_info`
WHERE `user_id` = %s"""


add_user_bookmark: str = """
INSERT INTO `users_bookmarks` (`user_id`, `bookmark_page`)
VALUES (%s, %s)"""


user_bookmarks_query: str = """
SELECT `bookmark_page`
FROM `users_bookmarks`
WHERE `user_id` = %s"""


del_user_bookmark: str = """
DELETE FROM `users_bookmarks`
WHERE `user_id` = %s AND `bookmark_page` = %s"""


add_admin_books: str = """
INSERT INTO `admin_books` (`file_tg_id`, `book_title`)
VALUES (%s, %s)"""


admin_books_query: str = """
SELECT `file_tg_id`, `book_name`
FROM `admin_books`
WHERE `admin_book_id` = %s"""


admin_books_count_query: str = """
SELECT COUNT(`admin_book_id`)
FROM `admin_books`"""