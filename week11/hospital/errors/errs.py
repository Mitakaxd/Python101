class UserAlreadyExistsError(Exception):
    pass
class DatabaseConnectionError(Exception):
    pass
class PasswordsDontMatchError(Exception):
    pass
class BadPasswordError(Exception):
    pass