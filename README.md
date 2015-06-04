# tutum-python-example [![Circle CI](https://circleci.com/gh/jackfirth/tutum-python-example.svg?style=svg)](https://circleci.com/gh/jackfirth/tutum-python-example)

Reference example Python web-app deployed with docker-compose and Tutum

The app is a simple webserver that uses a Redis container to count how many times it's been visited. App container code is in `./test`

# Setup

You'll need docker installed on your machine. If you're on Linux, this is easy, if youre on OS X, you'll want to use `boot2docker` or something wrapping it. If you're on Windows, may Cthulhu have mercy on your soul.

Once docker is installed, run `sudo pip install -U -r requirements.txt` from the project root to install `docker-compose` and testing/linting tools.

# Running

Run `docker-compose up` then go to `localhost:5000` in your browser (on OS X use the `boot2docker ip` instead of localhost).

# Testing

Unit tests are run with `nosetests ./app`. Integration tests are run through `docker-compose`, with a `test` container started up linked to the app container. Therefore whenever you change code, you'll need to rebuild with `docker-compose build app` or `docker-compose build test` before running integration tests. To actually run the integration tests, run `docker-compose run test`.

# CI setup

The CI lints code with `pep8`, runs unit tests on the app container code, then starts up the app and runs integration tests with `docker-compose run test`.

# Deployment

On successful runs on master, the app container image is pushed to Tutum and the running service is auto-redeployed. You can see the running app in "production" at http://http://web.tutum-python-example.jackfirth.svc.tutum.io
