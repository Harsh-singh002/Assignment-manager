from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('assignments.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM assignments ORDER BY due_date').fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        title = request.form['title']
        subject = request.form['subject']
        due_date = request.form['due_date']
        priority = request.form['priority']

        conn = get_db_connection()
        conn.execute('INSERT INTO assignments (title, subject, due_date, priority, status) VALUES (?, ?, ?, ?, ?)',
                     (title, subject, due_date, priority, 'Pending'))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/complete/<int:id>')
def complete(id):
    conn = get_db_connection()
    conn.execute('UPDATE assignments SET status = ? WHERE id = ?', ('Completed', id))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM assignments WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)