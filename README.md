# CRUD API DRF

This is the Back End for https://github.com/networkdavit/react_movie project

## Simple Web API
# ExpresJS/MongoDB API

## Description

This project was built to help you start express/mongo API with a boilerplate which is fully ready for most of the basic back end tasks such as authorization, authentication, email confirmation and CRUD

## Features

* Admin login (default credentials - test1, test12345)
* Registration 
* Authentication via JWT
* CRUD for movies from admin
* Displaying Movies

### Installing

```
git clone https://github.com/networkdavit/drf_api_movie.git
cd drf_api_movie

//Mac/Linux/Unix
python3 -m venv env
source env/bin/activate
pip3 install requirements.txt

//Windows
python -m venv env
.\env\Scripts\activate
pip install requirements.txt

python3 manage.py migrate
python3 manage.py runserver
```

## API Endpoints

To test the application
* POST http://localhost:8000/api/v1/auth/verify-token/
* POST http://localhost:8000/api/v1/auth/register/
* POST http://localhost:8000/api/v1/auth/token/
* POST http://localhost:8000/api/v1/auth/token/refresh
* GET/POST http://localhost:8000/api/v1/movies/
* GET/PATCH/DELETE http://localhost:8000/api/v1/movies/{id}

## Test API

* Via POST method register a user/admin  http://localhost:8000/api/v1/auth/register ,make sure to include json as payload to add to the db, example
```
{
	"first_name": "super",
	"last_name": "tester",
	"username": "supertester1",
	"email": "supertester1@gmail.com",
	"password": "supertester123",
	"password2": "supertester123"
}
```
* Via POST method login to get a token http://localhost:8000/api/v1/auth/token ,make sure to include json as payload to add to the db, example
```
{
	"username": "supertester1",
	"password": "supertester123"
}
```

* Via GET method retrieve all the movies http://localhost:8000/api/v1/movies/
* Via POST method add a new movie http://localhost:8000/api/v1/movies/, make sure to include json as payload to add to the db, example
```
{
	"title":"Venom",
	"genre": "Comics",
	"year": 2022
}
make sure to add Bearer token in the authorization header (Get the token from http://localhost:8000/api/v1/auth/token endpoint)

```
* Via GET method retrieve a single movie http://localhost:8000/api/v1/movies/{id}
* Via PATCH method retrieve update a single movie http://localhost:8000/api/v1/movies/{id}, make sure to include json as payload to add to the db, example
{
	"title":"Saw",
	"genre": "Horror",
	"year": 2020
}
make sure to add Bearer token in the authorization header (Get the token from http://localhost:8000/api/v1/auth/token endpoint)
* Via DELETE method retrieve delete a single movie http://localhost:8000/api/v1/movies/{id}
make sure to add Bearer token in the authorization header (Get the token from http://localhost:8000/api/v1/auth/token endpoint)