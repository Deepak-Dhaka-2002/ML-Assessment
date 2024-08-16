SELECT p.*
FROM posts p
JOIN friends f ON p.user_id = f.friend_id
WHERE f.user_id = 'current_user_id';
