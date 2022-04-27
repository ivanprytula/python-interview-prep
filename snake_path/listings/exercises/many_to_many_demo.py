"""
Three Kinds of Keys:
- *Primary key* - generally an integer auto-increment field
- *Logical key* - What the outside world uses for lookup
- *Foreign key* - generally an integer key pointing to a row in another table

Key Rules. Best practices:
- Never use your *logical key* as the *primary key*
- *Logical keys* can and do change, albeit slowly
- *Relationships* that are based on matching string fields are less efficient than integers

Foreign Keys:
- A *foreign key* is when a table has a column that contains a key which points to the *primary key* of another table.
- When all primary keys are integers, then all foreign keys are integers - this is good - very good
"""



import sqlite3

conn = sqlite3.connect('mtm.sqlite')
cur = conn.cursor()

cur.execute('''
    CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE,
    email  TEXT
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
);
''')

conn.commit()
cur.close()
