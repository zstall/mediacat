To run mediacat in docker do the following:

- Create a working directory and pull down the repo
- Run the command: `docker compose up -d`
- Once the conatiners are running, to configure the DB, get the ID of the non postgres container by running: `docker containers ls`
- Exec into the non db container: `docker exec -it <container id> sh`
- In the container command line, run: `psql postgresql://admin:admin@localhost:5432/mediacat -af mediacat.sql` This will create the needed tables
- To populate the DB and create an admin user, in the non db container then run: `python3 create_mediacat_db.py`
