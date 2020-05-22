from flask import Flask, render_template, url_for, request
from data import queries
import util, datetime

app = Flask('codecool_series')


@app.route('/shows')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/design')
def design():
    return render_template('design.html')


@app.route('/')
def list_shows():
    shows = queries.get_shows()

    return render_template('test.html', shows=shows)


@app.route('/show/<show_id>')
def show_detail(show_id):
    is_long = None
    show_episodes = queries.get_actual_show(show_id)
    if len(show_episodes) > 100:
        is_long = True
    else:
        is_long = False

    return render_template('show.html', episode=show_episodes, long=is_long)


@app.route('/actors')
def actors():
    top_ten_actors = queries.get_actors()
    acting_sum = util.shows_sum()

    return render_template('actors.html', actors=top_ten_actors, acting_sum=acting_sum)


@app.route('/season-detail', methods=['POST', 'GET'])
def season_detail():
    result_shows = None
    show_count = None
    if request.method == 'POST':
        if request.form['episode'] != "":
            episode = request.form['episode']
        else:
            episode = 0
        if request.form['season'] != "":
            season = request.form['season']
        else:
            season = 0

        result_shows = queries.search(episode, season)
        show_count = len(result_shows)

    return render_template('seasons.html', results=result_shows, count=show_count)


@app.route('/stars', methods=['GET', 'POST'])
def stars():
    detailed_shows = None
    if request.method == 'POST':
        target_genre = request.form['genre']
        detailed_shows = queries.show_detailed(target_genre)

    return render_template('stars.html', shows=detailed_shows)


@app.route('/year-cards')
def years():
    year_from_int = "19700101"
    year_from = datetime.datetime.strptime(year_from_int, '%Y%m%d')

    year_to_int = "20101231"
    year_to = datetime.datetime.strptime(year_to_int, '%Y%m%d')


    year_details = queries.year_detailed(year_from, year_to)

    return render_template('years.html', years=year_details)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
