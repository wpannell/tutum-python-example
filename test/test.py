import unirest


def assert_response(expected_response_body):
    response = unirest.get("http://web:5000")
    print 'Response =', response.body
    assert response.code == 200
    assert response.body == expected_response_body


if __name__ == "__main__":

    assert_response('''Hello World!
    I have been seen 1 times.
    I have been deployed 1 times.''')

    assert_response('''Hello World!
    I have been seen 2 times.
    I have been deployed 1 times.''')
