# Vinsany

A lightweight Python utility module for **data processing**, **HTTP requests**, and **browser operations**.

---

## 📦 Features

- ✅ Module initialization (`init`, `hello`)
- ✅ Send HTTP requests (`GET`, `POST`, `PUT`, `DELETE`)
- ✅ Open URLs in browser
- ✅ Basic statistical data analysis (mean, median, std_dev, max, min, sum)
- ✅ Analyze data (find max, min, repeated values)

---

## 🧩 API Reference

### `__init__.py`

- `init()` – Initialize the module
- `hello()` – Returns `"Hello World"` if initialized
- `hi()` – Alias of `hello()`

### `web.py`

- `send_get_request(url, params=None, headers=None)` – Send GET request
- `send_post_request(url, data=None, json=None, headers=None)` – Send POST request
- `send_put_request(url, data=None, json=None, headers=None)` – Send PUT request
- `send_delete_request(url, headers=None)` – Send DELETE request
- `Open_URL(url, mode="")` – Open URL in browser (`mode="new"`, `"new_tab"`, or `None`)

### `data_utils.py`

- `mean(data: List[Union[int, float]]) -> float` – Calculate the mean
- `median(data: List[Union[int, float]]) -> Union[int, float]` – Calculate the median
- `max_value(data: List[Union[int, float]]) -> Union[int, float]` – Return maximum value
- `min_value(data: List[Union[int, float]]) -> Union[int, float]` – Return minimum value
- `std_dev(data: List[Union[int, float]]) -> float` – Calculate standard deviation
- `total_sum(data: List[Union[int, float]]) -> Union[int, float]` – Return total sum
- `analyze_data(*data: Union[int, float]) -> Dict[str, Union[int, float, Dict[Union[int, float], int]]]` – Analyze data to find:
  - Maximum value
  - Minimum value
  - Repeated values and their counts

---

## 🧠 Data Analysis Function

### `analyze_data(*data: Union[int, float]) -> Dict[str, Union[int, float, Dict[Union[int, float], int]]]`

Analyzes the input data to find:

- The **maximum value**
- The **minimum value**
- The **repeated values** (values that appear more than once)

#### Example:

```python
result = analyze_data(3, 5, 2, 5, 7, 3, 9, 9, 9)
print(result)