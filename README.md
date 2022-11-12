# decoreq

**This package is currently a work in progress.**

Setup-less decorator-based friendly library for making HTTP requests.

## Introduction

The name `decoreq` comes from merging the words `decorator` and `request`.

The aim of this project is to make life easier for Python developer
who need to interact with any external service through HTTP.

Because it's meant to be easy to use, there's no setup needed. You can simply just start using it right away.

```python
from decoreq import decoreq, json, get


@decoreq
@json
@get('https://www.example.com/query')
def query(pid: int, tags: [str]):
    decoreq.request.urlparams.add(id=pid, tags=','.join(tags))

    def success():
        response = decoreq.response.body
        # Handle response ...

    def error():
        response = decoreq.response.body
        # Handle response ...

    return success, error
```