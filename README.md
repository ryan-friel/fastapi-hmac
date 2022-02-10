# Fastapi-hmac

This project will accept post data containing json to a specific endpoint. The json will then be used to generate an HMAC token which is then returned to the user.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Fastapi-hmac dependencies.
```bash
pip install -r requirements.txt
```

## Running the application

```bash
uvicorn main:app --reload
```

We can then send json data to the localhost:8000/generate-token endpoint. Be aware that only json objects will be accepted as specified in the requirements.
I imported the curl command into postman for testing purposes.

## Unit Tests

You can use the pytest module to views the unit tests created. They are located in the test_main.py
```bash
pytest
```
