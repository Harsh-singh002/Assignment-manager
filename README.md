# Student Assignment Management System

This is a simple web-based application built using Flask and SQLite that allows students to manage their assignments efficiently. Users can add, view, update, and delete assignments with due dates, priorities, and reminders.

## Features

- Add assignments with subject, due date, and priority
- Mark assignments as completed
- Delete assignments
- View all tasks in a clean, user-friendly dashboard
- Basic reminder and status update logic
- Responsive styling with CSS

## Technologies Used

- Python (Flask)
- HTML & CSS (Bootstrap-style layout)
- SQLite for data storage

## Installation

1. Clone the repository or download the ZIP file.
2. Navigate to the project directory and set up a virtual environment (optional):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install required packages:
   ```
   pip install flask
   ```
4. Create the SQLite database:
   ```
   sqlite3 assignments.db < schema.sql
   ```
5. Run the Flask app:
   ```
   python app.py
   ```

## Folder Structure

```
assignment_manager/
│
├── app.py
├── schema.sql
├── static/
│   └── style.css
└── templates/
    ├── index.html
    └── add.html
```

## License

This project is for educational purposes only.

## Author

Developed by a Computer Science student as part of an academic project.