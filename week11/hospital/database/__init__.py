import sqlite3
from database.create_database import *



class Database:

    def __init__(self):
        self.conn = sqlite3.connect("hospital.db")
        self.cursor = self.conn.cursor()
        for query in CREATE_TABLE_QUERYS:
            print(query)
            self.execute_query(query)

    def find_user(self, username, password):
        self.cursor.execute('SELECT username,password,status FROM users WHERE username=? AND password=?',(username,password))
        user = self.cursor.fetchone()
        return user

    def execute_query(self, query):
        self.cursor.execute(query)
        self.conn.commit()

    def create_user(self, username, hashed_pass, **kwargs):
        self.cursor.execute('INSERT INTO users(username,password) VALUES (?,?)', (username, hashed_pass))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
        

    #         self.db.get_reservations_for_doctor(self.username, self.password)
    #     else:
    #         self.db.get_reservations_for_patient(self.username, self.password)

    # @classmethod
    # def open_slot(cls, current_user, start_hour):
    #     current_user.clear_appointments(date, from_hour)
    #     current_user.clear_reservation(doctor_name, date)
    #     current_user.open_slot(date, start_hour)


    #     appointment = self.db.find_appointment(
    #         patient.username, doctor_name, date)
    #     if appointment == None:
    #         return None
    #     return cls(appointment['patient_full_name'], doctor_name, date, appointment['time'])
    #     Appointment.make_appointment(current_user, doc, date, start_time)
    #     Appointment.get_open_slots(doctor=doc, date=date)
