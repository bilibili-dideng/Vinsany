import webbrowser
from typing import Literal,TypeAlias

is_init = False

class NotInitializedError(Exception):
    pass

class MissingParametersError(Exception):
    pass

def init() -> None:
    global is_init
    is_init = True

def hello() -> str:
    if is_init:
        return "Hello World"
    else:
        raise NotInitializedError

def hi() -> None: hello()

def output(text) -> None: print(text)

def Open_URL(URL="",mode="") -> None:
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