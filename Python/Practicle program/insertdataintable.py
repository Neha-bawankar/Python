import sqlite3

# Connect to the database (or create it if it doesn't exist)
connection = sqlite3.connect("example.db")

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# Add the 'city' column if it doesn't already exist
cursor.execute("ALTER TABLE Users ADD COLUMN city TEXT")

# Function to insert records into the table
def insert_record(name, age, city):
    cursor.execute("INSERT INTO Users (name, age, city) VALUES (?, ?, ?)", (name, age, city))
    connection.commit()  # Save changes to the database
    print(f"Record inserted: {name}, {age}, {city}")

# Insert sample records
insert_record("Alice", 25, "New York")
insert_record("Bob", 30, "London")
insert_record("Charlie", 35, "Paris")

# Fetch and display records to verify insertion
cursor.execute("SELECT * FROM Users")
records = cursor.fetchall()
print("\nRecords in the table:")
for record in records:
    print(record)

# Close the connection
connection.close()