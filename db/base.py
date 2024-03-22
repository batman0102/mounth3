import sqlite3
from pathlib import Path

class Database:
    def __init__(self) -> None:
        db_path = Path(__file__).parent.parent / "list.sqlite"
        self.db = sqlite3.connect(db_path)
        self.cursor = self.db.cursor()

    def drop_tables(self):
        self.cursor.execute("DROP TABLE IF EXISTS movies")
        self.db.commit()

    def create_tables(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                description TEXT,
                year INTEGER,
                director TEXT
            )
            """
        )
        self.db.commit()

    def populate_tables(self):
        self.cursor.executescript(
            """
            INSERT INTO movies (title, description, year, director) 
            VALUES 
                ('Интерстеллар', 'Фильм о путешествиях в космосе', 2014, 'Кристофер Нолан'),
                ('Властелин колец', 'Эпическая сага о борьбе добра со злом', 2001, 'Питер Джексон');
            """
        )
        self.db.commit()

    def get_all_movies(self):
        self.cursor.execute("SELECT * FROM movies")
        return self.cursor.fetchall()


if __name__ == "__main__":
    db = Database()
    db.drop_tables()
    db.create_tables()
    db.populate_tables()
    movies = db.get_all_movies()
    for movie in movies:
        print(movie)
