from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__, static_folder='static', static_url_path='/src')

app.config['TEMPLATES_AUTO_RELOAD'] = True

def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            uid INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            age INTEGER,
            dob TEXT
        )
    """)
    conn.commit()
    conn.close()

@app.route("/", methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        name = request.form.get("name")
        email = request.form.get("email")
        age = request.form.get("age")
        dob = request.form.get("dob")

        if not email or not age.isdigit() or int(age) <= 0:
            error_message = "Invalid input. Please ensure all fields are filled correctly."
            return render_template('index.html', error=error_message)

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email, age, dob) VALUES (?, ?, ?, ?)", (name, email, age, dob))
        conn.commit()
        conn.close()
        return redirect('/users')

    return render_template('index.html')

@app.route('/users')
def users():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, email, age, dob FROM users")
    data = cursor.fetchall()
    conn.close()

    return render_template('users.html', data=data)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
