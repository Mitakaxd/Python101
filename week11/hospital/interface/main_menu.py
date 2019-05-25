from controller.main_controller import MainController


class MainMenu:

    @classmethod
    def default_method(cls, *args, **kwargs):
        print('HELP MENU')

    @classmethod
    def show_options(cls,  current_user):
        while True:
            print("Pick an option")
            option = input()
            method_name = OPTION_MENU.get(option, cls.default_method)
            method_name(**{'current_user': current_user})
        # TODO decide what you want in this dict

        # if option == '1':
        #     members = MainController.show_members(current_user)
        #     cls._pretty_print_members(members)

    @classmethod
    def show_appointments(cls, current_user):
        MainController.show_members(current_user)

    @classmethod
    def _pretty_print_members(cls, members):
        for member in members:
            print('{status} {username}'.format(
                status=getattr(member, 'status', ''),
                username=member.username))

    @classmethod
    def available_slots(**kwargs):
        date = input('Date[dd::mm]: ')
        print(MainController.request_avaiable_times(date=date, doctor=None))

    @classmethod
    def patient_make_reservation(**kwargs):
        doc = input('Specify doctor:')
        date = input('Date[dd::mm]: ')
        start_time = input('Hour: ')
        try:
            Validations.validate_doctor_name(doc)
        except DoctorDoesntExistError:
            exit(1)
        saved_reservation = MainController.requestReservation(
            current_user, doc, date, start_time)
        if saved_reservation:
            print('Success')
        else:
            print('Reservation unsuccessfull, doctors avaiable times for same date:')
            print(MainController.request_avaiable_times(doctor=doc, date=date))

    @classmethod
    def doctor_open_slots(**kwargs):
        if not current_user.is_doctor:
            exit(1)
        date = input('Working day[dd::mm]: ')
        start_time = input('start_hour: ')
        end_hour = input('End_hour: ')
        MainController.log_doctor_workday(
            current_user, date, start_time, start_hour)

    def patient_cancel_appointment(**kwargs):
        doctor_name = input('doctor: ')
        date = input('date[dd::mm]: ')
        try:
            appointment = MainController.get_appointment_info(
                current_user, doctor_name, date)
        except Exception:
            exit(1)
        MainController.remove_appointment(current_user, doctor_name, date)

    def doctor_clear_workday(**kwargs):
        if not current_user.is_doctor:
            exit(1)
        date = input("Working day[dd::mm]: ")
        end_hour = input("Clear after hour: ")
        MainController.clear_hours(current_user, date, end_hour)
OPTION_MENU = {
        '1': MainMenu.show_appointments,
        '2': MainMenu.available_slots,
        '3': MainMenu.patient_make_reservation,
        '4': MainMenu.doctor_open_slots,
        '6': MainMenu.patient_cancel_appointment,
        '7': MainMenu.doctor_clear_workday

    }
