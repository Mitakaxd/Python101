from database.__init__ import Database

class User:
    db = Database()

    def __init__(self, username, password, status=None):
        self.username = username
        self.password = password
        self._status = status

    @classmethod
    def find(cls, username, password):
        result = cls.db.find_user(username, password)
        if result:
            return cls(username, password, result[2])

    @classmethod
    def create_new_user(cls, username, hashed_pass, **kwargs):
        try:
            # TODO check kwargs
            cls.db.create_user(username, hashed_pass, **kwargs)
        except DatabaseConnectionError:
            sys.exit(1)
        return cls(username, hashed_pass, **kwargs)

    @property
    def is_doctor():
        return self._status != ''

    def get_appointments(self):
        if self.is_doctor:
            self.db.get_reservations_for_doctor(self.username)
        else:
            self.db.get_reservations_for_patient(self.username)

    def open_slot(self, start_hour):
        if self.is_doctor:
            self.__class__.db.insert_slot(self.username,start_hour)
    def clear_appointments(self,date,from_hour):
        if self.is_doctor:
            self.__class__.db.clear_slots(self.username,date,from_hour)
    def clear_reservation(self,doctor_name,date):
        if not self.is_doctor:
            self.__class__.db.clear_appointment(self.name,doctor_name,date)

class Appointment:

    def __init__(self, patient, doctor, date, time):
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time

    @classmethod
    def find(cls, patient, doctor_name, date):
        appointment = patient.__class__.db.find_appointment(
            patient.username, doctor_name, date)
        if appointment == None:
            return None
        return cls(appointment['patient_full_name'], doctor_name, date, appointment['time'])
    @classmethod
    def make_appointment(cls,current_user,doc,date,start_hour):
        pass
    @classmethod
    def get_open_slots(cls, current_user, doctor, date):
        pass
