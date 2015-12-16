# API-Lovely
 
This Quickstart guide will show you how to use Compose to run a Python3.4/PostgreSQL API. Before starting, you’ll need to have Compose installed (see more details below).

 
## Development enviroment 
### Requirements

You must have both [Docker](https://docs.docker.com/) (or a
[Docker Machine](https://docs.docker.com/machine/) host) and
[Docker Compose](https://docs.docker.com/compose/) running on your machine.

You can find instructions for the recommended setup on
[Linux](doc/DOCKER_SETUP_ON_LINUX.md), [Mac OSX](doc/DOCKER_SETUP_ON_MAC.md) and
[Windows 8+](doc/DOCKER_SETUP_ON_WINDOWS.md).


### Run containers

The next step to run our containers is build them. for this
you need to run:

	docker-compose build

To spin up our containers:

	docker-compose up

Stopping the containers:

	docker-compose stop

### Usage

Check the running app web interface with the IP you receive from you Docker machine with port 8000

Example:
	
	http://192.168.99.100:8000


##### Creating an user in the API
For using the API, you need a valid user and password in the database.

	docker-compose run api python3 manage.py createsuperuser
	
If you need a shell, run:

	docker-compose run api python3 manage.py shell
	
##### Testing the API
After you created and user and password, now you can test the API with this new credentials.

	curl -H 'Content-Type: application/json; indent=4' -u USERNAME_HERE:PASSWORD_HERE -X POST -d '{"beds": 2, "baths": 1, "address": "123 Some St, Gotham, IL 51944", "provider_name": "RentingIsTheBestAround", "price": 750}' http://192.168.99.100:8000/listings/

## Production enviroment 
