add_user_info_query: str = """
INSERT INTO `users_info` (`user_id`, `page`)
VALUES (%s, %s)"""