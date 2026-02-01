import sqlite3

connection = sqlite3.connect('jobs.db')

# ဤနေရာတွင် encoding='utf8' ကို ထည့်သွင်းပေးရပါမည်
with open('schema.sql', encoding='utf8') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# နမူနာဒေတာများ (မြန်မာစာပါလည်း အဆင်ပြေစေရန်)
cur.execute("INSERT INTO jobs (title, location, salary, phone, description) VALUES (?, ?, ?, ?, ?)",
            ('Factory Worker', 'Bangkok', '15,000 THB', '0812345678', 'စက်ရုံအလုပ်သမား အရေးပေါ်အလိုရှိသည်။')
            )

connection.commit()
connection.close()
print("Database initialized successfully!")