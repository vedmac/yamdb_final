[![Actions Status](https://github.com/Bytlot/yamdb_final/workflows/CI/badge.svg)](https://github.com/Bytlot/yamdb_final/actions)
# Service Yamdb

Service – databases of reviewing films, books, music and REST API for it 

## Getting Started

Clone this repository: 
```
git clone https://github.com/Bytlot/yamdb_final.git
```

### Prerequisites

Requirements before start:

[Docker](https://docs.docker.com/get-docker/)

[Docker-compose](https://docs.docker.com/compose/install/)

Set your environment with your settings in `.env` file:
```
# SAMPLE
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

### Installing

Installing steps:

Build and run:
```
$ make start
```
Collect static:
```
$ make collectstatic
```
Make migration:
```
$ make migration
```
Fill database from fixtures:
``` 
$ make filldb
```
Create supruser:
```
$ make createsuperuser
```
Stop:
```
$ make stop
```

## Admin access

Admin panel available after project started at http://localhost/admin/


## API Documentation

API Documentation available after project started at http://localhost/redoc

## Built With

Project powered Django, PostgreSQL, Gunicorn and NGINX


## Authors

* **Viktor Ermolov** - *Initial work* - (https://github.com/Bytlot)

## License

This project is licensed under the MIT License.

## Acknowledgments

Yandex.Praktikum
