from flask import Flask, render_template, request, redirect, url_for, session, send_file, jsonify
import sqlite3
import pandas as pd
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

# Admin credentials
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'password'


# Route for student form
@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    semester = request.form['semester']
    major = request.form['major']
    netid = request.form['netid']
    email = request.form['email']
    purpose = request.form['purpose']
    
    # Get the current date and time (for submission timestamp)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Ensure format is correct

    # Save the data to the database
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO students (name, semester, major, netid, email, purpose, timestamp) 
            VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (name, semester, major, netid, email, purpose, timestamp))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

    # Render the same form page with a success message
    return render_template('form.html', message='Form submitted successfully!')




# Admin login page
@app.route('/admin', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            return redirect(url_for('admin_dashboard'))
        else:
            return 'Invalid Credentials, please try again.'

    return render_template('admin_login.html')

# Admin Dashboard
@app.route('/admin/dashboard')
def admin_dashboard():
    if 'admin_logged_in' in session:
        try:
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM students")
            students = cursor.fetchall()  # Fetch all students from the database
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            conn.close()

        # No need to create an extra 'display ID'—just use the real ID
        return render_template('admin_dashboard.html', students=students)
    else:
        return redirect(url_for('admin_login'))

    

# Route to render the "Add Student" form page
@app.route('/admin/add')
def render_add_student_page():
    return render_template('add_student.html')

# This function handles the POST request to add the student to the database
@app.route('/admin/add_student', methods=['POST'])
def handle_add_student():
    name = request.form.get('name')
    semester = request.form.get('semester')
    major = request.form.get('major')
    netid = request.form.get('netid')
    email = request.form.get('email')  # Make sure the email is captured here
    purpose = request.form.get('purpose')

    # Proceed with your logic for saving the student to the database
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (name, semester, major, netid, email, purpose, timestamp) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (name, semester, major, netid, email, purpose, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

    return redirect(url_for('admin_dashboard'))




# This route deletes a student from the database
@app.route('/admin/delete/<int:student_id>', methods=['POST'])
def delete_student(student_id):
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
        conn.commit()
        print(f"Successfully deleted student with ID: {student_id}")
    except sqlite3.Error as e:
        print(f"Error while deleting student: {e}")
    finally:
        conn.close()

    return redirect(url_for('admin_dashboard'))



# Route to download the data as Excel
@app.route('/admin/download')
def download_data():
    if 'admin_logged_in' in session:
        try:
            conn = sqlite3.connect('database.db')
            df = pd.read_sql_query("SELECT * FROM students", conn)
            df.to_excel('students_data.xlsx', index=False)
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            conn.close()
        
        return send_file('students_data.xlsx', as_attachment=True)
    else:
        return redirect(url_for('admin_login'))
    
# Route to serve filtered student data dynamically
@app.route('/admin/filter_data', methods=['POST'])
def filter_data():
    start_date = request.form.get('start_date')
    end_date = request.form.get('end_date')

    if start_date and end_date:
        try:
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM students WHERE date(timestamp) BETWEEN ? AND ?", (start_date, end_date))
            students = cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            conn.close()

        # Return the data in JSON format
        return jsonify(students)
    return jsonify([])

# Admin logout
@app.route('/logout')
def logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('admin_login'))


if __name__ == "__main__":
    app.run(debug=True)
