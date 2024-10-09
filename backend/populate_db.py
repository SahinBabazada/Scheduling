import sqlite3

DATABASE = 'schedule.db'

def connect_db():
    return sqlite3.connect(DATABASE)

def populate_db():
    employees = [
        ('AS1396', 'Tahirov Nizami', 'HRIS Manager', 'HR', 3, 6),
        ('AS1332', 'Həsənov Xəyal', 'HRIS Manager', 'HR', 3, 1),
        ('AS1313', 'Yusif Huseynzada', 'HRIS Manager', 'HR', 6, 2),
        ('AS1376', 'Shahin Babazada', 'HRIS Manager', 'HR', 4, 7)
    ]
    
    schedules = [
        ('06-08-24', 'AS1396', '08:00 - 19:00', '07:45 - 19:53', 'M'),
        ('07-08-24', 'AS1396', '08:00 - 19:00', '09:56 - 18:56', 'M'),
        # Add the rest of the schedule data here...
    ]
    
    conn = connect_db()
    cursor = conn.cursor()
    cursor.executemany('''
        INSERT INTO employees (badge, name, position, department, bayram_balansi, mezuniyyet_balansi)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', employees)
    
    cursor.executemany('''
        INSERT INTO schedules (date, badge, plan, fakt, mezuniyyet_qrafiki)
        VALUES (?, ?, ?, ?, ?)
    ''', schedules)
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    populate_db()
