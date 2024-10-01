import sqlite3

# Create db and table
def create_database():
    conn = sqlite3.connect('alerts.db')
    cursor = conn.cursor()

    # Table for storing alerts
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()

create_database()