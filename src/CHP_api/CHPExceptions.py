import typing as t

# CHP_adapter #############
class LoginException(AttributeError):
    def __init__(self, string_message: str):
        self.txt = string_message
###########################


# ChpClient ###############
class ApiConnectionError(RuntimeError):
    def __init__(self, string_message: str, data: t.Optional[t.Union[t.List, t.Dict]] = None):
        self.txt = string_message
        self.resp_data = data
