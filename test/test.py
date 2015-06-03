import unirest


def assert_response(expected_response_body):
    response = unirest.get('http://web:5000')
    assert response.code == 200
    assert response.body == expected_response_body

assert_response("Hello World! I have been seen 1 times.")
assert_response("Hello World! I have been seen 2 times.")
