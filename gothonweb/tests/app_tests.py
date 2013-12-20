from nose.tools import *
from bin.app import app
from tests.tools import assert_response


def test_index():
    # Check that we get a 404 on the / URL
    resp = app.request("/")
    assert_response(resp, status="404")

    # Test our first GET request to /hello
    resp = app.request("/hello")
    assert_response(resp)

    # Make sure default values work for the form
    resp = app.request("/hello", method="POST")
    assert_response(resp, contains="Nobody")

    # Test that we get expected values
    data = {'name': 'Zed', 'greet': 'Hola'}
    resp = app.request("/hello", method="POST", data=data)
    assert_response(resp, contains="Zed")
