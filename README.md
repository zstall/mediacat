To run mediacat in docker do the following:

- Create a working directory and pull down the repo
- create a file named `database.ini` and configure it with the following:
```
[mediaCatDB]
host=postgres
database=mediacat 
user=admin
password=admin
```
*NOTE*: you can change these values, but this will then need to be updated throughout the application

*NOTE*: Docker is required to run this application
- Run the command: `docker compose up -d`
- Once the conatiners are running, to configure the DB, get the ID of the non postgres container by running: `docker containers ls`
- Exec into the non db container: `docker exec -it <container id> sh`
- In the container command line, run: `psql postgresql://admin:admin@localhost:5432/mediacat -af mediacat.sql` This will create the needed tables
- To populate the DB and create an admin user, in the non db container then run: `python3 create_mediacat_db.py`

This is a demo applicatoin, and will be running on `localhost:5000`. To login into the application use username: `admin` and password `admin`

*NOTE*: Docker image can be found here: https://hub.docker.com/repository/docker/zstall/mediacat-flask-app/general
