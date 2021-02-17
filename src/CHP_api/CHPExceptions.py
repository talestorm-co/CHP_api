import typing as t


# CHP_adapter ################################################################################################
class LoginException(AttributeError):
    def __init__(self, string_message: str):
        self.txt = string_message


##############################################################################################################



# ChpClient ##################################################################################################

class ChpError(RuntimeError):
    def __init__(self, msg: str, data: t.Optional[t.Union[t.List, t.Dict, str]] = None):
        self.txt = msg
        self.resp_data = data

class ApiConnectionError(ChpError):
    pass

class ApiRequestException(ChpError):
    pass

class ApiResponseNotJson(ChpError):
    pass

##############################################################################################################
