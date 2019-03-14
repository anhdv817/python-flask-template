## FLASK RESTFUL API BOILERPLATE
### Start app with docker
#### Prerequisites
- Os: Windows or Linux
- Docker
- Docker-compose

#### Start app for development
- Copy .env.example => .env
- Edit mapping port, or environment if need
- Run `docker-compose up`
- Open http://localhost:{APP_PORT}/api . Enjoy!

#### Deployment
- Copy .env.example => .env
- Edit mapping port, or environment if need
- Copy docker-compose.override.sample.yml => docker-compose.override.yml
- Run `docker-compose up`

### Console commands

- To run application: `flask run`

### Database migration

1. Initiate a migration folder (once only)

```bash
flask db init
```

2. Create migration script from detected changes in the model
```bash
flask db migrate --message 'initial database migration'
```

3. Apply the migration script to the database
```bash
flask db upgrade
``` 

### Viewing the app ###

Open the following url on your browser to view swagger documentation
[http://127.0.0.1:5000/](http://127.0.0.1:5000/)
### Application folder structure
#### Split by modules
Separate components of our app into a group of inter-connected modules  
:file_folder: /docs: external documentation  
:file_folder: /etc: app configurations, gunicorn config, logging, nginx  
:file_folder: /migrations: db migration scripts  
:file_folder: /module 1: sources of module 1   
:file_folder: /module 2: sources of module 2   

#### Module structure
Each module is spitted by repository pattern
##### Repository Pattern
![alt text](https://i.imgur.com/cNUvEwZ.png "Repository Pattern")


##### Module folder structure
:file_folder: /api: define api url, request body, params  
:file_folder: /commands: define flask command  
:file_folder: /extensions: setup base configuration  
:file_folder: /helpers: define helper function  
:file_folder: /models: define orm model  
:file_folder: /repositories: define repository to access data  
:file_folder: /services: handle business logic  
:file_folder: /tests: app test script  

### 📙 Resource

#### Libraries
- Flask http://flask.pocoo.org/  
- Flask restplus: document api https://flask-restplus.readthedocs.io/en/stable/  
- Pytest: testing framework https://docs.pytest.org/en/latest/
- SqlAlchemy: orm http://flask-sqlalchemy.pocoo.org/2.3/

### Contributing
If you want to contribute to this boilerplate, clone the repository and just start making pull requests.
