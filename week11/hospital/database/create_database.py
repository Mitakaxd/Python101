import sqlite3


CREATE_TABLE_USERS = """
    CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username VARCHAR(60), password VARCHAR(100),
    status VARCHAR(10),
    fullname TEXT)
    """

CREATE_TABLE_PATIENTS = """
    CREATE TABLE IF NOT EXISTS patients(id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,status_p VARCHAR(60), address VARCHAR(100),age INTEGER, FOREIGN KEY(user_id) REFERENCES users(id))
    """

CREATE_TABLE_DOCTORS = """
    CREATE TABLE  IF NOT EXISTS doctors(doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
     user_id INTEGER, FOREIGN KEY(user_id) REFERENCES users(id))
    """


CREATE_TABLE_RESERVATIONS = """
    CREATE TABLE IF NOT EXISTS reservations(reservation_id INTEGER PRIMARY KEY AUTOINCREMENT, patient_id INTEGER,slot_id INTEGER,status VARCHAR(10),
    FOREIGN KEY(patient_id) REFERENCES patients(id), 
     FOREIGN KEY(slot_id) REFERENCES slots(id))
    """
CREATE_TABLE_SLOTS = """
    CREATE TABLE IF NOT EXISTS slots(id INTEGER PRIMARY KEY AUTOINCREMENT, doctor_id INTEGER,start_hour VARCHAR(10), end_hour VARCHAR(10), day VARCHAR(10),
     FOREIGN KEY(doctor_id) REFERENCES doctors(doctor_id))
    """
CREATE_TABLE_QUERYS = [CREATE_TABLE_USERS, CREATE_TABLE_PATIENTS,
                       CREATE_TABLE_DOCTORS, 
                        CREATE_TABLE_SLOTS,CREATE_TABLE_RESERVATIONS]
