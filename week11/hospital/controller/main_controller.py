from hospital.user import User,Appointment
from errors.errs import BadPasswordError,UserAlreadyExistsError

class MainController:

    @classmethod
    def _validate_password(cls,password):
        for ch in password:
            if ch not in '0123456789':
                exit(1)

    @classmethod
    def _hash_password(cls,password):
        return password
    @classmethod
    def sign_in(cls, username, password):
        cls._validate_password(password)
        password = cls._hash_password(password)
        current_user = User.find(username, password)
        return current_user

    @classmethod
    def _do_passwords_match(cls,pass1,pass2):
        return pass1==pass2
    @classmethod
    def sign_up(cls, username, password, second_password):
        cls._validate_password(password)
        cls._validate_password(second_password)

        hashed_pass1 = cls._hash_password(password)
        hassed_pass2 = cls._hash_password(second_password)
        cls._do_passwords_match(hashed_pass1, hassed_pass2)

        if User.find(username, password):
            raise UserAlreadyExistsError

        return User.create_new_user(username, hashed_pass1)

    @classmethod
    def show_members(cls, current_user):
        if current_user.is_doctor:
            return cls.show_patients(current_user)
            #  [Patient('Roza'), Patient('Mimi')]
        else:
            return cls.show_doctors(current_user)

    @classmethod
    def show_patients(cls,current_user):
        return current_user.get_appointments()
    @classmethod
    def show_doctors(cls,current_user):
        return current_user.get_appointments()
    @classmethod
    def clear_hours(cls,current_user,date,from_hour):
        if  not current_user.is_doctor:
            raise UserNotADoctorError
        current_user.clear_appointments(date,from_hour)

    @classmethod
    def remove_appointment(current_user,doctor_name,date):
        if  not current_user.is_doctor:
            current_user.clear_reservation (doctor_name,date)

    @classmethod
    def get_appointment_info(cls,current_user,doctor_name,date):
        appointment = Appointment.find(current_user,doctor_name,date)
        return appointment
    @classmethod
    def log_doctor_workday(cls, current_user, date, start_hour, end_hour):
        if current_user.is_doctor:
            for hour in range(start_hour,end_hour):
                current_user.open_slot(date, start_hour)
    @classmethod
    def request_avaiable_times(cls, doctor, date):
        return Appointment.get_open_slots(doctor, date)

    @classmethod
    def requestReservation(cls,current_user, doc, date, start_time):
        times = MainController.request_avaiable_times(doc,date)
        if start_time in times:
            Appointment.make_appointment(current_user,doc,date,start_time)
            return True
        else:
            return False