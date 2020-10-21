
class LoginException(AttributeError):
    def __init__(self, string_message: str):
        self.txt = string_message