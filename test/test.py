import unirest


response = unirest.get('http://web:5000')

assert response.code == 200

assert response.body == "Hello World! I have been seen 1 times."
