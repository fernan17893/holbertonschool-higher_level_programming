-- list all shows in hbtn_0d_tvshows without a genre linked
-- must be in ascending order by tv_shows.title - tv_show_genres.genre_id
SELECT t.`title`, g.`genre_id`
  FROM `tv_shows` AS t
       LEFT JOIN `tv_show_genres` AS g
       ON t.`id` = g.`show_id`
       WHERE g.`genre_id` is NULL
ORDER BY t.`title`, g.`genre_id`;
