import sqlite3
import json
from models import Entry, Mood

def get_all_entries():
   
    with sqlite3.connect("./dailyjournal.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.date,
            e.concept,
            e.entry,
            e.mood_id,
            m.label
        FROM Entry e
        JOIN Mood m
            ON m.id = e.mood_id
        """)

        entries = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            entry = Entry(row['id'], row['date'], row['concept'],
                            row['entry'], row['mood_id'])
            
            mood = Mood(row['id'], row['label'])

            entry.mood = mood.__dict__

            entries.append(entry.__dict__)

    return json.dumps(entries)

def get_single_entry(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.date,
            e.concept,
            e.entry,
            e.mood_id,
            m.label
        FROM Entry e
        JOIN Mood m
            ON m.id = e.mood_id
        WHERE e.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        entry = Entry(data['id'], data['date'], data['concept'],
                            data['entry'], data['mood_id'])
        
        mood = Mood(data['mood_id'], data['label'])

        entry.mood = mood.__dict__

    return json.dumps(entry.__dict__)

def delete_entry(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM entry
        WHERE id = ?
        """, (id, ))

def search_entry(searchText):
    with sqlite3.connect("./dailyjournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.date,
            e.concept,
            e.entry,
            e.mood_id
        FROM Entry e
        WHERE e.entry LIKE ?
        """, (f"%{searchText}%", ))

        entries = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            entry = Entry(row['id'], row['date'], row['concept'],
                            row['entry'], row['mood_id'])

            entries.append(entry.__dict__)

    return json.dumps(entries)

def create_entry(new_entry):
    with sqlite3.connect("./dailyjournal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Entry
            ( date, concept, entry, mood_id )
        VALUES
            ( ?, ?, ?, ?);
        """, (new_entry['date'], new_entry['concept'], new_entry['entry'],
                    new_entry['mood_id'], ))
        
        id = db_cursor.lastrowid

        new_entry['id'] = id
    
    return json.dumps(new_entry)