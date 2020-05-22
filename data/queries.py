from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_actual_show(show_id):
    return data_manager.execute_select(
        'SELECT episodes.title, episodes.episode_number FROM seasons INNER JOIN episodes ON episodes.season_id = seasons.id WHERE seasons.show_id=%(show_id)s;',
        {'show_id': show_id})


def get_actors():
    return data_manager.execute_select(
        'SELECT  actors.name, COUNT(show_characters.actor_id) AS CNT FROM show_characters INNER JOIN actors ON actors.id = show_characters.actor_id GROUP BY actors.id, actors.name ORDER BY COUNT(*) DESC ;')


def search(episode_num, season_num):
    return data_manager.execute_select(
        'SELECT shows.title FROM shows INNER JOIN seasons ON seasons.show_id = shows.id INNER JOIN episodes ON episodes.season_id = seasons.id WHERE seasons.season_number >= %(season_num)s AND episodes.episode_number >= %(episode_num)s GROUP BY shows.title' , {'episode_num':episode_num, 'season_num':season_num})


def show_detailed(genre):
    return data_manager.execute_select('SELECT shows.title, shows.year, shows.rating FROM shows INNER JOIN show_genres ON show_genres.show_id = shows.id  INNER JOIN genres ON genres.id = show_genres.genre_id WHERE genres.name = %(genre)s  ORDER BY rating DESC ', {'genre':genre})

def year_detailed(yearfrom,yearto):
    return data_manager.execute_select('SELECT year, AVG(rating) AS rating, COUNT(id) AS shows FROM shows WHERE  year > %(yearfrom)s AND year < %(yearto)s  GROUP BY year ORDER BY year DESC ', {'yearfrom':yearfrom, 'yearto':yearto})