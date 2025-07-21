import requests
import webbrowser

def send_post_request(url, data=None, json=None, headers=None):
    """
    General function for sending POST requests

    :param url: Request URL
    :param data: Form data (dict)
    :param json: JSON data (dict)
    :param headers: Request header (dict)
    :return: Response object
    """
    try:
        response = requests.post(
            url,
            data=data,
            json=json,
            headers=headers
        )
        response.raise_for_status()  # 如果响应码不是 2xx，抛出异常
        return response
    except requests.exceptions.RequestException as e:
        print(f"request failure: {e}")
        return None

def send_put_request(url, data=None, json=None, headers=None):
    """
    General function for sending PUT requests

    :param url: Request URL
    :param data: Form data (dict)
    :param json: JSON data (dict)
    :param headers: Request header (dict)
    :return: Response object
    """
    try:
        response = requests.put(url, data=data, json=json, headers=headers)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"PUT request failure: {e}")
        return None

def send_delete_request(url, headers=None):
    """
    General function for sending DELETE requests

    :param url: Request URL
    :param data: Form data (dict)
    :param json: JSON data (dict)
    :param headers: Request header (dict)
    :return: Response object
    """
    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"DELETE request failure: {e}")
        return None

def send_get_request(url, params=None, headers=None):
    """
    General function for sending GET requests

    :param url: Request URL
    :param data: Form data (dict)
    :param json: JSON data (dict)
    :param headers: Request header (dict)
    :return: Response object
    """
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"GET request failure: {e}")
        return None

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