is_init = False

class NotInitializedError(Exception):
    pass

class MissingParametersError(Exception):
    pass

def init() -> None:
    """
    Initialized the module
    :return: None
    """
    global is_init
    is_init = True

def hello_world() -> str:
    """
    :return: "Hello World"
    """
    if is_init:
        return "Hello World"
    else:
        raise NotInitializedError
