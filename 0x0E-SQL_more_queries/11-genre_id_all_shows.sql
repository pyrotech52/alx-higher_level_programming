-- lists all shows contained in the database hbtn_0d_tvshows
SELECT s.title, t.genre_id FROM tv_shows s LEFT JOIN tv_show_genres t ON s.id = t.show_id ORDER BY s.title, t.genre_id;
