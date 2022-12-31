import sqlite3


def reset_db():
    # Connect to the database
    conn = sqlite3.connect('users.db')

    # Delete all rows from all tables
    conn.execute("DROP TABLE users;")

    # Commit the transaction
    conn.commit()

    # Close the connection
    conn.close()
