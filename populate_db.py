import sqlite3
from all_pickup_lines_list import all_pickup_lines

# def main():
#     populate_language_table()
#     populate_category_table()


# def populate_language_table():
#     with sqlite3.connect("db.sqlite3") as connection:
#         cursor = connection.cursor()

#         execute_query = lambda query, params=None: cursor.execute(
#             query, params
#         ).fetchone()

#         language_dictionary = {}
#         for pickup_line in all_pickup_lines:
#             language = pickup_line["language"]
#             if language not in language_dictionary:
#                 language_query = "SELECT id, language FROM language WHERE language = ?"
#                 result = execute_query(language_query, (language,))
#                 print(result)

#                 if result is None:
#                     insert_language_query = "INSERT INTO language(language) VALUES(?)"
#                     cursor.execute(insert_language_query, (language,))

#                     result = execute_query(
#                         "SELECT id FROM language ORDER BY id DESC LIMIT 1"
#                     )

#                     language_dictionary[language] = result[0]

#                 else:
#                     language_dictionary[language] = result[0]
#                 break


# def populate_category_table():
#     with sqlite3.connect("db.sqlite3") as connection:
#         cursor = connection.cursor()

#         execute_query = lambda query, params=None: cursor.execute(
#             query, params
#         ).fetchone()

#     category_dictionary = {}
#     for pickup_line in all_pickup_lines:
#         category = pickup_line["category"]
#         if category not in category_dictionary:
#             category_query = "SELECT id, category FROM category WHERE category = ? "
#             result = execute_query(category_query, (category,))
#             print(result)

#         if result is None:
#             insert_category_query = "INSERT INTO category(category) VALUES(?)"
#             cursor.execute(insert_category_query, (category,))

#             result = execute_query("SELECT id FROM category ORDER BY id DESC LIMIT 1")

#             category_dictionary[category] = result[0]
#         else:
#             category_dictionary[category] = result[0]
#         break


# if __name__ == "__main__":
#     main()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS language (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            language TEXT UNIQUE
        )
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS category (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT UNIQUE
        )
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS pickup_line (
            id TEXT PRIMARY KEY,
            text TEXT,
            category_id INTEGER,
            language_id INTEGER,
            dateCreated TEXT,
            FOREIGN KEY (category_id) REFERENCES category(id),
            FOREIGN KEY (language_id) REFERENCES language(id)
        )
    """
    )

    connection.commit()


def populate_tables():
    with sqlite3.connect("db.sqlite3") as connection:
        create_tables(connection)
        cursor = connection.cursor()

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
