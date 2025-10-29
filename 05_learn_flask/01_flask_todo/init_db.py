import sqlite3
connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())
cur = connection.cursor()

tasks = [
('Learn Flask', 'Complete the Flask tutorial', 0),
('Build a project', 'Create a todo application', 0),
('Deploy app', 'Deploy the application online', 0),
]

# Insert sample tasks
cur.executemany("INSERT INTO tasks (title, description, completed) VALUES (?, ?, ?)",
tasks
)
connection.commit()
connection.close()
print("Database initialized successfully!")