import sqlite3


def main():
    all = retrieve_pickup_lines()
    print(all)


# Function to retrieve pickup_lines
def retrieve_pickup_lines():
    with sqlite3.connect("db.sqlite3") as connection:
        cursor = connection.cursor()

        query = """
            SELECT
                pickup_line.text,
                language.language AS language,
                category.category AS category
            FROM
                pickup_line
            JOIN
                language ON pickup_line.language_id = language.id
            JOIN
                category ON pickup_line.category_id = category.id
        """

        cursor.execute(query)

        # Fetching all result
        pickup_lines = cursor.fetchall()

        formatted_data = [
            {"text": line[0], "language": line[1], "category": line[2]}
            for line in pickup_lines
        ]

        return formatted_data


if __name__ == "__main__":
    main()
