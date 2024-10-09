# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from werkzeug.security import generate_password_hash, check_password_hash

# app = Flask(__name__)
# CORS(app)

# users = {
#     "testuser": generate_password_hash("testuser")
# }

# # Time options to be served to the frontend
# time_options = [
#     { 'value': '06:30-15:30', 'label': '06:30-15:30', 'color': '#EAE3C8', 'shift': 'Səhər' },
#     { 'value': '07:00-16:00', 'label': '07:00-16:00', 'color': '#CFC5A5', 'shift': 'Səhər' },
#     { 'value': '07:30-16:30', 'label': '07:30-16:30', 'color': '#E3D18A', 'shift': 'Səhər' },
#     { 'value': '08:00-17:00', 'label': '08:00-17:00', 'color': '#BD9354', 'shift': 'Səhər' },
#     { 'value': '08:00-13:00', 'label': '08:00-13:00', 'color': '#9E7540', 'shift': 'Səhər' },
#     { 'value': '09:00-18:00', 'label': '09:00-18:00', 'color': '#D8EFD3', 'shift': 'Səhər' },
#     { 'value': '10:00-19:00', 'label': '10:00-19:00', 'color': '#95D2B3', 'shift': 'Səhər' },
#     { 'value': '11:00-20:00', 'label': '11:00-20:00', 'color': '#55AD9B', 'shift': 'Günorta' },
#     { 'value': '12:00-21:00', 'label': '12:00-21:00', 'color': '#F1F8E8', 'shift': 'Günorta' },
#     { 'value': '12:30-21:30', 'label': '12:30-21:30', 'color': '#116A7B', 'shift': 'Günorta' },
#     { 'value': '13:00-22:00', 'label': '13:00-22:00', 'color': '#CDC2AE', 'shift': 'Gecə' },
#     { 'value': '13:30-22:30', 'label': '13:30-22:30', 'color': '#6096B4', 'shift': 'Gecə' },
#     { 'value': '14:00-23:00', 'label': '14:00-23:00', 'color': '#DBA39A', 'shift': 'Gecə' },
#     { 'value': '14:30-23:30', 'label': '14:30-23:30', 'color': '#F0DBDB', 'shift': 'Gecə' },
#     { 'value': '15:00-23:59', 'label': '15:00-23:59', 'color': '#F5EBE0', 'shift': 'Gecə' },
#     { 'value': '16:00-21:00', 'label': '16:00-21:00', 'color': '#BA94D1', 'shift': 'Günorta' },
#     { 'value': '17:00-01:00', 'label': '17:00-01:00', 'color': '#BCCEF8', 'shift': 'Gecə' },
#     { 'value': '22:00-07:00', 'label': '22:00-07:00', 'color': '#92A9BD', 'shift': 'Gecə' },
#     { 'value': '22:00-08:00', 'label': '22:00-08:00', 'color': '#E4CDA7', 'shift': 'Gecə' },
#     { 'value': '22:30-07:30', 'label': '22:30-07:30', 'color': '#D3E4CD', 'shift': 'Gecə' },
#     { 'value': '23:59-09:00', 'label': '23:59-09:00', 'color': '#C37B89', 'shift': 'Gecə' },
#     { 'value': 'Bayram', 'label': 'Bayram', 'color': '#000000', 'shift': 'Bayram' },
#     { 'value': 'Məzuniyyət', 'label': 'Məzuniyyət', 'color': '#000000', 'shift': 'Bayram' }
# ]

# # Sample user-specific schedule data
# user_schedule_data = {
#     "AS1396": {
#         "2024-08-06": {"value": "07:00-16:00", "label": "07:00-16:00", "color": "#CFC5A5"},
#         "2024-08-07": {"value": "08:00-17:00", "label": "08:00-17:00", "color": "#BD9354"},
#         "2024-08-08": {"value": "09:00-18:00", "label": "09:00-18:00", "color": "#D8EFD3"},
#         "2024-08-09": {"value": "08:00-13:00", "label": "08:00-13:00", "color": "#9E7540"},
#         "2024-08-10": {"value": "08:00-17:00", "label": "08:00-17:00", "color": "#BD9354"},
#         "2024-08-11": {"value": "09:00-18:00", "label": "09:00-18:00", "color": "#D8EFD3"},
#         "2024-08-12": {"value": "09:00-18:00", "label": "09:00-18:00", "color": "#D8EFD3"}
#     }
#     # Add more user-specific data here
# }

# @app.route('/user_schedule/<user_id>', methods=['GET'])
# def get_user_schedule(user_id):
#     user_schedule = user_schedule_data.get(user_id, {})
#     return jsonify(user_schedule)

# @app.route('/time_options', methods=['GET'])
# def get_time_options():
#     return jsonify(time_options)

# @app.route('/login', methods=['POST'])
# def login():
#     data = request.json
#     username = data.get('username')
#     password = data.get('password')
#     if username in users and check_password_hash(users[username], password):
#         return jsonify({"message": "Login successful", "status": "success"})
#     else:
#         return jsonify({"message": "Invalid credentials", "status": "fail"}), 401

# if __name__ == '__main__':
#     app.run(debug=True)


from flask_cors import CORS
from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)
CORS(app)

time_options = [
    { 'value': '06:30-15:30', 'label': '06:30-15:30', 'color': '#EAE3C8', 'shift': 'Səhər' },
    { 'value': '07:00-16:00', 'label': '07:00-16:00', 'color': '#CFC5A5', 'shift': 'Səhər' },
    { 'value': '07:30-16:30', 'label': '07:30-16:30', 'color': '#E3D18A', 'shift': 'Səhər' },
    { 'value': '08:00-17:00', 'label': '08:00-17:00', 'color': '#BD9354', 'shift': 'Səhər' },
    { 'value': '08:00-13:00', 'label': '08:00-13:00', 'color': '#9E7540', 'shift': 'Səhər' },
    { 'value': '09:00-18:00', 'label': '09:00-18:00', 'color': '#D8EFD3', 'shift': 'Səhər' },
    { 'value': '10:00-19:00', 'label': '10:00-19:00', 'color': '#95D2B3', 'shift': 'Səhər' },
    { 'value': '11:00-20:00', 'label': '11:00-20:00', 'color': '#55AD9B', 'shift': 'Günorta' },
    { 'value': '12:00-21:00', 'label': '12:00-21:00', 'color': '#F1F8E8', 'shift': 'Günorta' },
    { 'value': '12:30-21:30', 'label': '12:30-21:30', 'color': '#116A7B', 'shift': 'Günorta' },
    { 'value': '13:00-22:00', 'label': '13:00-22:00', 'color': '#CDC2AE', 'shift': 'Gecə' },
    { 'value': '13:30-22:30', 'label': '13:30-22:30', 'color': '#6096B4', 'shift': 'Gecə' },
    { 'value': '14:00-23:00', 'label': '14:00-23:00', 'color': '#DBA39A', 'shift': 'Gecə' },
    { 'value': '14:30-23:30', 'label': '14:30-23:30', 'color': '#F0DBDB', 'shift': 'Gecə' },
    { 'value': '15:00-23:59', 'label': '15:00-23:59', 'color': '#F5EBE0', 'shift': 'Gecə' },
    { 'value': '16:00-21:00', 'label': '16:00-21:00', 'color': '#BA94D1', 'shift': 'Günorta' },
    { 'value': '17:00-01:00', 'label': '17:00-01:00', 'color': '#BCCEF8', 'shift': 'Gecə' },
    { 'value': '22:00-07:00', 'label': '22:00-07:00', 'color': '#92A9BD', 'shift': 'Gecə' },
    { 'value': '22:00-08:00', 'label': '22:00-08:00', 'color': '#E4CDA7', 'shift': 'Gecə' },
    { 'value': '22:30-07:30', 'label': '22:30-07:30', 'color': '#D3E4CD', 'shift': 'Gecə' },
    { 'value': '23:59-09:00', 'label': '23:59-09:00', 'color': '#C37B89', 'shift': 'Gecə' },
    { 'value': 'Bayram', 'label': 'Bayram', 'color': '#000000', 'shift': 'Bayram' },
    { 'value': 'Məzuniyyət', 'label': 'Məzuniyyət', 'color': '#000000', 'shift': 'Bayram' }
]

@app.route('/time_options', methods=['GET'])
def get_time_options():
    return jsonify(time_options)

DATABASE = 'schedule.db'

def connect_db():
    return sqlite3.connect(DATABASE)

def init_db():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                badge TEXT PRIMARY KEY,
                name TEXT,
                position TEXT,
                department TEXT,
                bayram_balansi INTEGER,
                mezuniyyet_balansi INTEGER
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS schedules (
                date TEXT,
                badge TEXT,
                plan TEXT,
                fakt TEXT,
                mezuniyyet_qrafiki TEXT,
                FOREIGN KEY (badge) REFERENCES employees (badge)
            )
        ''')
        conn.commit()

@app.route('/employees', methods=['GET'])
def get_employees():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees')
    employees = cursor.fetchall()
    conn.close()
    return jsonify(employees)

@app.route('/schedules', methods=['GET'])
def get_schedules():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM schedules')
    schedules = cursor.fetchall()
    conn.close()
    return jsonify(schedules)

@app.route('/add_employee', methods=['POST'])
def add_employee():
    data = request.json
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO employees (badge, name, position, department, bayram_balansi, mezuniyyet_balansi)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (data['badge'], data['name'], data['position'], data['department'], data['bayram_balansi'], data['mezuniyyet_balansi']))
    conn.commit()
    conn.close()
    return jsonify({'status': 'success'}), 201

@app.route('/add_schedule', methods=['POST'])
def add_schedule():
    data = request.json
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO schedules (date, badge, plan, fakt, mezuniyyet_qrafiki)
        VALUES (?, ?, ?, ?, ?)
    ''', (data['date'], data['badge'], data['plan'], data['fakt'], data['mezuniyyet_qrafiki']))
    conn.commit()
    conn.close()
    return jsonify({'status': 'success'}), 201

if __name__ == '__main__':
    init_db()
    app.run(debug=True)



