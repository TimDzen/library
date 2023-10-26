from datetime import datetime

from flask import Flask, request, redirect, url_for
from flask import render_template

from database import db, Book, Genre

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()

    genre1 = Genre(name='Роман')
    genre2 = Genre(name='Ужасы')
    db.session.add_all([genre1, genre2])
    db.session.commit()

    books = []
    for _ in range(15):
        book1 = Book(title='Книга романа {}'.format(_),
                     author='Автор романа {}'.format(_),
                     genre_id=genre1.id,
                     created_at=datetime.utcnow()
                     )
        book2 = Book(title='Книга ужасов {}'.format(_),
                     author='Автор книги {}'.format(_),
                     genre_id=genre2.id,
                     created_at=datetime.utcnow()
                     )
        books.extend([book1, book2])

    db.session.add_all(books)
    db.session.commit()


@app.route('/')
def index():
    books = Book.query.order_by(Book.created_at.desc()).limit(15).all()
    return render_template('index.html', books=books)


@app.route('/genre/<int:genre_id>')
def genre(genre_id):
    genre = Genre.query.get_or_404(genre_id)
    books = Book.query.filter_by(genre_id=genre_id).all()
    return render_template('genre.html',
                           genre=genre,
                           books=books
                           )


@app.route("/update_status", methods=['POST'])
def update_status():
    book_id = request.form.get('book_id')
    is_read = request.form.get('is_read')
    book = Book.query.get_or_404(book_id)
    book.is_read = is_read
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
