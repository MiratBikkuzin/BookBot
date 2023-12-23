add_user_info_query: str = """
INSERT INTO `users_info` (`user_id`, `page`)
VALUES (%s, %s)"""


update_user_page_query: str = """
UPDATE `users_info`
SET `page` = %s"""


select_user_info_query: str = """
SELECT `user_id`, `page`
FROM `users_info`
WHERE `user_id` = %s"""


select_user_bookmarks_query: str = """
SELECT `bookmark_page`
FROM `user_bookmarks`
WHERE `user_id` = %s"""