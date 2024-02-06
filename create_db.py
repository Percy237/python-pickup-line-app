import sqlite3

create_language_query = """
    CREATE TABLE language(id integer PRIMARY KEY AUTOINCREMENT, language TEXT)
"""

create_category_query = """
    CREATE TABLE category(id integer PRIMARY KEY AUTOINCREMENT, category TEXT)
"""
create_pickup_line_query = """
    CREATE TABLE pickup_line(
    id TEXT PRIMARY KEY,
    text TEXT, 
    category_id integer, 
    language_id integer, 
    dateCreated TEXT,
    FOREIGN KEY (category_id) REFERENCES category(id) 
    FOREIGN KEY (language_id) REFERENCES language(id) 
    )
"""

with sqlite3.connect("db.sqlite3") as connection:
    cursor = connection.cursor()
    for statement in [
        create_language_query,
        create_category_query,
        create_pickup_line_query,
    ]:
        cursor.execute(statement)
