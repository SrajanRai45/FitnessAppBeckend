import pandas
from datetime import datetime
import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('user_data.db' , check_same_thread=False)
cursor = conn.cursor()

# Create a table to store entries
cursor.execute('''
    CREATE TABLE IF NOT EXISTS entries (
        entry_date TEXT NOT NULL,
        processed_value REAL NOT NULL
    )
''')
conn.commit()

# Function to add a new entry
def add_entry(date_str, value):
    try:
        cursor.execute('INSERT INTO entries (entry_date, processed_value) VALUES (?, ?)', (date_str, value))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"⚠️ An error occurred while inserting: {e}")
        return False


def get_data(target_date):
    cursor.execute("SELECT processed_value FROM entries WHERE entry_date = ?", (target_date,))
    return cursor.fetchall()


def update_data(data, date):
    try:
        cursor.execute("UPDATE entries SET processed_value = ? WHERE entry_date = ?", (data, date))
        conn.commit()
        if cursor.rowcount == 0:
            print(f"ℹ️ No records found with entry_date = {date}. No update performed.")
        else:
            print(f"✅ Successfully updated {cursor.rowcount} record(s) with entry_date = {date}.")
    except sqlite3.Error as e:
        print(f"⚠️ An error occurred while updating: {e}")


def delete_data(date):
    try:
        cursor.execute("DELETE FROM entries WHERE entry_date = ?", (date,))
        conn.commit()
        if cursor.rowcount > 0:
            print(f"✅ Successfully deleted records with entry_date = {date}")
            return True
        else:
            print(f"⚠️ No records found with entry_date = {date}")
            return False
    except sqlite3.Error as e:
        print(f"⚠️ An error occurred: {e}")
        return False




def alldata():
    cursor.execute("SELECT * FROM entries")
    conn.commit()
    return cursor.fetchall()

# Example usage
today = datetime.now().strftime('%Y-%m-%d')
#add_entry(today, 42.5) 
#delete_data('2025-04-21')
#update_data(300 , today)
#result =(get_data(today))[0][0]
#alldata()
print(alldata())