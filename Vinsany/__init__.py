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

def hello() -> str:
    """
    :return: "Hello World"
    """
    if is_init:
        return "Hello World"
    else:
        raise NotInitializedError

def hi() -> None:
    """
    :return: "Hello World"
    """
    hello()
