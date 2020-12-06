import typing as t


# CHP_adapter ################################################################################################
class LoginException(AttributeError):
    def __init__(self, string_message: str):
        self.txt = string_message


##############################################################################################################


# ChpClient ##################################################################################################
class ApiConnectionError(RuntimeError):
    def __init__(self, msg: str, data: t.Optional[t.Union[t.List, t.Dict]] = None):
        self.txt = msg
        self.resp_data = data


class ApiRequestException(RuntimeError):
    def __init__(self, msg: str, data: t.Optional[t.Union[t.List, t.Dict]] = None):
        self.txt = msg
        self.resp_data = data

##############################################################################################################
