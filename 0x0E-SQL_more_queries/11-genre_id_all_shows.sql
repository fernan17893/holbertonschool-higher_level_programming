-- lists all shows contained in hbtn_0d_tvshows
-- Each record should display tv_shows.title - tv_show_genres.genre_id
SELECT t.`title`, g.`genre_id`
  FROM `tv_shows` AS t
       LEFT JOIN `tv_show_genres` AS g
       ON t.`id` = g.`show_id`
ORDER BY t.`title`, g.`genre_id` ASC;
