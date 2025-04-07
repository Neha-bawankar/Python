import sqlite3

# Connect to database
connection = sqlite3.connect("example.db")
cursor = connection.cursor()

# Delete a record by ID
cursor.execute("DELETE FROM Users WHERE id = ?", (2,))
connection.commit()  # Save changes

# Show remaining records
cursor.execute("SELECT * FROM Users")
print(cursor.fetchall())

connection.close()