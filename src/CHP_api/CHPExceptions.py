# CHP_adapter #############
class LoginException(AttributeError):
    def __init__(self, string_message: str):
        self.txt = string_message
###########################


# ChpClient ###############
class ApiConnectionError(RuntimeError):
    def __init__(self, string_message: str):
        self.txt = string_message
