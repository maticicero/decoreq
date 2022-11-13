# decoreq

**This package is currently a work in progress.**

Setup-less decorator-based friendly library for making HTTP requests.

## Introduction

The name `decoreq` comes from merging the words `decorator` and `request`.

The aim of this project is to make life easier for Python developers
who need to interact with any service through HTTP.

Because it's meant to be easy to use, there's no setup needed. You can simply just start using it right away.

```python
from decoreq import decoreq, session, json, post, get


@json  # Send and expect to receive JSON data
@post  # Send POST request to the endpoint with the same name as the function (i.e. /login)
def login(username: str, password: str):
    # Add both username and password to the request data to be sent
    decoreq.request.data.add(username=username, password=password)

    # Callback for a succesful response
    def on_success():
        # Retrieve the response JSON body
        response = decoreq.response.body

        # Extract the authentication token out of the response
        token = response['token']

        # Add an authorization header for the whole session
        decoreq.session.headers.add('Authorization', f'Bearer {token}')

    # Callback for a failure response
    def on_error():
        # Retrieve the response JSON body
        response = decoreq.response.body

        # Extract the authentication token out of the response
        reason = response['reason']

        # Raise an exception
        raise InvalidCredentials(reason)

    return on_success, on_error


@json  # Expect to receive JSON data
@get('/view-product-details')  # Send GET request to the specified endpoint
def view_product_details(pid: int):
    # Add the product ID to the URL parameters
    decoreq.request.urlparams.add(product_id=pid)

    # Callback for a response
    def on_response():
        # Check if the response was succesful
        is_succesful = decoreq.response.success

        # Raise an exception if response was not succesful
        if not is_succesful:
            raise ProductNotFound(pid)

        # Retrieve the response JSON body
        response = decoreq.response.body

        # Extract and return the product details
        return response['details']

    return on_response


@session  # Begins a session which allows for a shared context between multiple decorated calls
def get_product_price(pid: int):
    # Login and get the necessary credentials
    login(_USERNAME, _PASSWORD)

    # Get the product details
    product_details = view_product_details(pid)

    # Return the product's price
    return product_details['price']



```