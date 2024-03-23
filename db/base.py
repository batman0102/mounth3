import sqlite3
from pathlib import Path

class Database:
    def __init__(self) -> None:
        db_path = Path(__file__).parent.parent / "list.sqlite"
        self.db = sqlite3.connect(db_path)
        self.cursor = self.db.cursor()

    def drop_tables(self):
        self.cursor.execute("DROP TABLE IF EXISTS movies")
        self.cursor.execute("DROP TABLE IF EXISTS movies_categories")
        self.db.commit()

    def create_tables(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS movies_categories(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT
            )
            """
        )
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                description TEXT,
                year INT,
                director TEXT,
                category_id INTEGER,
                FOREIGN KEY (category_id) REFERENCES movies_categories (id)
            )
            """
        )
        self.db.commit()

    def populate_tables(self):
        self.cursor.execute(
            """
            INSERT INTO movies_categories (title)
            VALUES  ('Космос'),
                    ('Фэнтези'),
                    ('Комедия')
            """
        )
        self.cursor.execute(
            """
            INSERT INTO movies (title, description, year, director, category_id) 
            VALUES  ('Интерстеллар', 'Фильм о путешествиях в космосе', 2014, 'Кристофер Нолан', 1),
                    ('Властелин колец', 'Эпическая сага о борьбе добра со злом', 2001, 'Питер Джексон', 2),
                    ('Однажды в Голливуде', 'Комедия о золотом веке Голливуда в конце 60-х', 2019, 'Квентин Тарантино', 3),
                    ('Гарри Поттер и философский камень', 'История о юном волшебнике, который поступает в Школу чародейства и волшебства Хогвартс', 2001, 'Крис Коламбус', 2),
                    ('Гравитация', 'Астронавтки оказываются одни в открытом космосе после катастрофы.', 2013, 'Альфонсо Куарон', 1),
                    ('Марсианин', 'Астронавт Марк Уотни оказался забыт на Марсе своей командой и пытается выжить.', 2015, 'Ридли Скотт', 1),
                    ('Из машины', 'Молодой программист выбирает уединенный дом в горах для секретного эксперимента по созданию искусственного интеллекта.', 2014, 'Алекс Гарленд', 3),
                    ('Джентльмены', 'Американский экспат пытается продать свою империю наркотиков в Лондоне, вызывая кучу проблем с заговорами, схемами, выкупом и вымогательством.', 2019, 'Гай Ричи', 3)
            """
        )
        self.db.commit()

    def get_movies_by_category(self, category_id):
        self.cursor.execute(
            """
            SELECT movies.id, movies.title, movies.description, movies.year, movies.director
            FROM movies
            JOIN movies_categories ON movies.category_id = movies_categories.id
            WHERE movies_categories.id = ?
            """,
            (category_id,)
        )
        return self.cursor.fetchall()

    def get_all_movies(self):
        self.cursor.execute(
            """
            SELECT id, title, description, year, director FROM movies
            """
        )
        return self.cursor.fetchall()


if __name__ == "__main__":
    db = Database()
    db.drop_tables()
    db.create_tables()
    db.populate_tables()
    movies = db.get_movies_by_category(2)
    for movie in movies:
        print(movie)
