# Flask web service with REST API
Simple web service working with this public API: https://jservice.io/api/random?count=1. 
Service is accepted a POST request with amount of questions to getting. 
All received questions are stored in the PostgreSQL DB. 
Response on this request will contain the last but one question. Service works inside docker containers.
## Utilizing Docker

### Project setup

Create `.env` file in the repository root:

```bash
cp .env.dev .env
```

Make adjustments to the environment variables as needed.

### Building of images and startup of containers

Run command in the repository root:

```bash
docker-compose up
```

This process may take several minutes first time.

### Stopping of containers

To stop containers ran command:

```bash
docker-compose stop
```

### Project initialization

The commands are executed inside the application container:

```bash
docker-compose exec app bash
```

#### Applying migrations (at first running):

```bash
flask db upgrade
```

#### Request example to the service POST API:
```bash
curl --header "Content-Type: application/json" --request POST --data '{"questions_num":3}'  http://localhost:5000
```
Note: number questions_num must be less than 100

### Connecting to DB
```bash
docker-compose exec db psql flask_db -U myuser
```
flask_db - DB name, myuser - DB user name

#### Show list all question table rows:
```bash
SELECT * FROM question;
```

#### Show count all question table rows:
```bash
SELECT COUNT(*) FROM question;
```

#### Delete all rows from question table:
```bash
TRUNCATE TABLE question;
```

