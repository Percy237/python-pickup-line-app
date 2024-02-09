import sqlite3
from all_pickup_lines_list import all_pickup_lines
from create_db import create_category_query
from create_db import create_language_query
from create_db import create_pickup_line_query


def populate_tables():
    with sqlite3.connect("db.sqlite3") as connection:
        cursor = connection.cursor()
        for statement in [
            create_language_query,
            create_category_query,
            create_pickup_line_query,
        ]:
            cursor.execute(statement)

        for pickup_line in all_pickup_lines:
            # Insert or retrieve language ID
            language_query = "SELECT id FROM language WHERE language = ?"
            language_id = cursor.execute(
                language_query, (pickup_line["language"],)
            ).fetchone()

            if language_id is None:
                cursor.execute(
                    "INSERT INTO language(language) VALUES (?)",
                    (pickup_line["language"],),
                )
                language_id = cursor.lastrowid
            else:
                language_id = language_id[0]

            # Insert or retrieve category ID
            category_query = "SELECT id FROM category WHERE category = ?"
            category_id = cursor.execute(
                category_query, (pickup_line["category"],)
            ).fetchone()

            if category_id is None:
                cursor.execute(
                    "INSERT INTO category(category) VALUES (?)",
                    (pickup_line["category"],),
                )
                category_id = cursor.lastrowid
            else:
                category_id = category_id[0]

            # Insert pickup line with foreign keys
            cursor.execute(
                """
                INSERT INTO pickup_line(id, text, category_id, language_id, dateCreated)
                VALUES (?, ?, ?, ?, ?)
            """,
                (
                    pickup_line["_id"],
                    pickup_line["text"],
                    category_id,
                    language_id,
                    pickup_line["dateCreated"],
                ),
            )

        connection.commit()


if __name__ == "__main__":
    populate_tables()
