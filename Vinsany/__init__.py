import webbrowser

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

def output(text) -> None:
    """
    :return: None
    """
    print(text)

def Open_URL(URL="",mode="") -> None:
    """
    Open a URL in the default browser
    :param URL:
    :param mode: new or new_tab or "" or None
    :return:
    """
    if URL == "":
        raise MissingParametersError
    else:
        if mode == "new":
            webbrowser.open_new(URL)
        if mode == "new_tab":
            webbrowser.open_new_tab(URL)
        if mode == "" or mode is None:
            webbrowser.open(URL)
        else:
            raise ValueError(f"Invalid mode : {"new","new_tab","",None}")