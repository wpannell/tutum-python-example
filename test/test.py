import unirest


response = unirest.get('http://web:5000')

assert response.code == 200
