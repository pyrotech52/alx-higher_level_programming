-- lists all shows contained in hbtn_0d_tvshows without a genre linked.
SELECT s.title, t.genre_id FROM tv_shows s LEFT JOIN tv_show_genres t ON s.id = t.show_id WHERE t.genre_id IS NULL ORDER BY s.title, t.genre_id;
