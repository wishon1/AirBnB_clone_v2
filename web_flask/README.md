# AirBnB Clone v2

This repository contains a Flask web application for the AirBnB clone project.

## Installation

## Resorces:
- Read or watch:

- [What is a Web Framework?](https://intelegain-technologies.medium.com/what-are-web-frameworks-and-why-you-need-them-c4e8806bd0fb)
- [A Minimal Application](https://flask.palletsprojects.com/en/2.3.x/quickstart/#a-minimal-application)
- [Routing (except “HTTP Methods”](https://flask.palletsprojects.com/en/2.3.x/quickstart/#routing)
- [Rendering Templates](https://flask.palletsprojects.com/en/2.3.x/quickstart/#rendering-templates)
- [Synopsis](https://jinja.palletsprojects.com/en/2.9.x/templates/#synopsis)
- [Variables](https://jinja.palletsprojects.com/en/2.9.x/templates/#variables)
- [Comments](https://jinja.palletsprojects.com/en/2.9.x/templates/#comments)
- [Whitespace Control](https://jinja.palletsprojects.com/en/2.9.x/templates/#whitespace-control)
- [List of Control Structures (read up to “Call”)](https://jinja.palletsprojects.com/en/2.9.x/templates/#list-of-control-structures)
- [Flask](https://palletsprojects.com/p/flask/)
- [Jinja](https://jinja.palletsprojects.com/en/2.9.x/templates/)

### 0. Hello Flask!

- File: `web_flask/0-hello_route.py`
- Description: This script starts a Flask web application listening on `0.0.0.0` port `5000` and displays "Hello HBNB!" when accessing the root route `/`.
- Command to run:
  ```
  python3 -m web_flask.0-hello_route
  ```

### 1. HBNB

- File: `web_flask/1-hbnb_route.py`
- Description: This script starts a Flask web application listening on `0.0.0.0` port `5000` and displays "Hello HBNB!" when accessing the root route `/`, and "HBNB" when accessing the route `/hbnb`.
- Command to run:
  ```
  python3 -m web_flask.1-hbnb_route
  ```

### 2. C is fun!

- File: `web_flask/2-c_route.py`
- Description: This script starts a Flask web application listening on `0.0.0.0` port `5000` and displays "Hello HBNB!" when accessing the root route `/`, "HBNB" when accessing the route `/hbnb`, and "C " followed by the value of the text variable when accessing the route `/c/<text>`.
- Command to run:
  ```
  python3 -m web_flask.2-c_route
  ```

### 3. Python is cool!

- File: `web_flask/3-python_route.py`
- Description: This script starts a Flask web application listening on `0.0.0.0` port `5000` and displays "Hello HBNB!" when accessing the root route `/`, "HBNB" when accessing the route `/hbnb`, "C " followed by the value of the text variable when accessing the route `/c/<text>`, and "Python " followed by the value of the text variable when accessing the route `/python/<text>`.
- Command to run:
  ```
  python3 -m web_flask.3-python_route
  ```

### 4. Is it a number?

- File: `web_flask/4-number_route.py`
- Description: This script starts a Flask web application listening on `0.0.0.0` port `5000` and displays "Hello HBNB!" when accessing the root route `/`, "HBNB" when accessing the route `/hbnb`, "C " followed by the value of the text variable when accessing the route `/c/<text>`, "Python " followed by the value of the text variable when accessing the route `/python/<text>`, and "n is a number" only if n is an integer when accessing the route `/number/<n>`.
- Command to run:
  ```
  python3 -m web_flask.4-number_route
  ```

### 5. Number template

- File: `web_flask/5-number_template.py`, `templates/5-number.html`
- Description: This script starts a Flask web application listening on `0.0.0.0` port `5000` and displays "Hello HBNB!" when accessing the root route `/`, "HBNB" when accessing the route `/hbnb`, "C " followed by the value of the text variable when accessing the route `/c/<text>`, "Python " followed by the value of the text variable when accessing the route `/python/<text>`, "n is a number" only if n is an integer when accessing the route `/number/<n>`, and a HTML page with the number when accessing the route `/number_template/<n>`.
- Command to run:
  ```
  python3 -m web_flask.5-number_template
  ```

### 6. Odd or even?

- File: `web_flask/6-number_odd_or_even.py`, `templates/6-number_odd_or_even.html`
- Description: This script starts a Flask web application listening on `0.0.0.0` port `5000` and displays "Hello HBNB!" when accessing the root route `/`, "HBNB" when accessing the route `/hbnb`, "C " followed by the value of the text variable when accessing the route `/c/<text>`, "Python " followed by the value of the text variable when accessing the route `/python/<text>`, "n is a number" only if n is an integer when accessing the route `/number/<n>`, a HTML page with the number when accessing the route `/number_template/<n>`, and a HTML page indicating whether the number is odd or even when accessing the route `/number_odd_or_even/<n>`.
- Command to run:
  ```
  python3 -m web_flask.6-number_odd_or_even
  ```

### 7. Improve engines

Before using Flask to display our HBNB data, you will need to update some parts of our engine:
- Update `FileStorage`: Add a public method `close(self)` to call `reload()` method for deserializing the JSON file to objects.
- Update `DBStorage`: Add a public method `close(self)` to call `remove()` method on the private session attribute (`self.__session`).
- Update `State`: If your storage engine is not `DBStorage`, add a public getter method `cities` to return the list of `City` objects from storage linked to the current `State`.

