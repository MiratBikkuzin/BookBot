add_user_info_query: str = """
INSERT INTO `users_info` (`user_id`, `page`)
VALUES (%s, %s)"""


select_user_info_query: str = """
SELECT `user_id`, `page`
FROM `users_info`
WHERE `user_id` = %s"""