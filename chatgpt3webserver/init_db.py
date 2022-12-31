import sqlite3


def init_db():
    # Connect to the database
    conn = sqlite3.connect('users.db')

    # Load the schema from the file
    with open('chatgpt3webserver/schema.sql', 'r') as f:
        schema = f.read()

    # Execute the schema in the database
    conn.executescript(schema)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
