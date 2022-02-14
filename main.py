from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests

from config import TMDB_API_KEY, SECRET_KEY

TMDB_SEARCH_URL = 'https://api.themoviedb.org/3/search/movie'
TMDB_DETAILS_URL = 'https://api.themoviedb.org/3/movie/'
TMDB_IMG_URL = 'https://image.tmdb.org/t/p/w500'


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
Bootstrap(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=True)
    description = db.Column(db.String(100), nullable=True)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(100), nullable=True)
    img_url = db.Column(db.String(150), nullable=True)


class UpdateForm(FlaskForm):
    rating = FloatField('Your Rating out of 10, e.g. 7.5', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Done')
    
    
class AddForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')

# db.create_all()


def sort_by_ranking() -> None:
    movies = Movie.query.order_by(Movie.rating.desc()).all()
    print(movies)
    for i in range(len(movies)):
        movies[i].ranking = i + 1
    db.session.commit()
    
        
@app.route("/")
def home():
    sort_by_ranking()
    all_movies = Movie.query.order_by(Movie.ranking).all()
    return render_template("index.html", movies=all_movies)


@app.route('/update', methods=['GET', 'POST'])
def update():
    movie_id = int(request.args.get('movie_id'))
    movie = Movie.query.get(movie_id)
    update_form = UpdateForm()
    if update_form.validate_on_submit():
        new_rating = update_form.rating.data
        new_review = update_form.review.data
        movie.rating = new_rating
        movie.review = new_review
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', movie=movie, form=update_form)
    
    
@app.route('/delete', methods=['GET', 'POST'])
def delete():
    movie_id = int(request.args.get('movie_id'))
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=['GET', 'POST'])
def add():
    add_form = AddForm()
    movie_tmdb_id = request.args.get('movie_tmdb_id')
    if movie_tmdb_id:
        params = {'api_key': TMDB_API_KEY}
        res = requests.get(f'{TMDB_DETAILS_URL}/{int(movie_tmdb_id)}', params=params).json()
        new_movie = Movie(title=res['title'], year=res['release_date'],
                          description=res['overview'], img_url=f'{TMDB_IMG_URL}{res["poster_path"]}')
        db.session.add(new_movie)
        db.session.commit()
        movie = Movie.query.filter_by(title=res['title']).first()
        return redirect(url_for('update', movie_id=movie.id))
    if add_form.validate_on_submit():
        title = add_form.title.data
        return redirect(url_for('select', title=title))
    return render_template('add.html', form=add_form)


@app.route('/select', methods=['GET', 'POST'])
def select():
    title = request.args.get('title')
    params = {'api_key': TMDB_API_KEY, 'query': title}
    response = requests.get(f'{TMDB_SEARCH_URL}', params=params).json()['results']
    return render_template('select.html', result=response)


if __name__ == '__main__':
    app.run(debug=True)
