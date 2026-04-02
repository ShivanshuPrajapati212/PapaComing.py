import sqlite3

# Path to your Zen Browser history database
db_path = r"/Users/shivanshu/Library/Application Support/zen/Profiles/6rqv2vcc.Default (release)/places.sqlite"

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

query = """
SELECT url, title, visit_count, last_visit_date
FROM moz_places
ORDER BY last_visit_date DESC
"""

cursor.execute(query)

for row in cursor.fetchall():
    print(row)

cursor.execute("DELETE FROM moz_historyvisits;")
cursor.execute("DELETE FROM moz_places;")

conn.commit()

print(f"Nuked {len(cursor.fetchall())} evidence")

conn.close()
