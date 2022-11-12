# decoreq

**This package is currently a work in progress.**

Setup-less decorator-based friendly library for making HTTP requests.

## Introduction

The name `decoreq` comes from merging the words `decorator` and `request`.

The aim of this project is to make life easier for Python developer
who need to interact with any external service through HTTP.

Because it's meant to be easy to use, there's no setup needed. You can simply just start using it right away.

```python
from decoreq import decoreq, json, post


@decoreq
@json
@post('/login')
def login(username: str, password: str):
    decoreq.request.data.add(username=username, password=password)

    def success():
        auth_token = decoreq.response.body['token']
        decoreq.session.headers.add('Authorization', f'Bearer {auth_token}')

    def error():
        message = decoreq.response.body['message']
        raise InvalidCredentials(message)

    return success, error
```