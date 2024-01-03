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