CREATE TABLE assignments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    subject TEXT NOT NULL,
    due_date TEXT NOT NULL,
    priority TEXT NOT NULL,
    status TEXT NOT NULL
);