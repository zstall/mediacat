# Running MediaCat in Docker

To run MediaCat in Docker, follow these steps:

1. **Create a working directory** and pull down the repository.
2. **Create a file** named `database.ini` in your working directory and configure it with the following:

   ```ini
   [mediaCatDB]
   host=postgres
   database=mediacat 
   user=admin
   password=admin
   ```

   **NOTE**: You can change these values, but they will need to be updated throughout the application.

   **NOTE**: Docker is required to run this application.

3. **Start the Docker containers** by running:

   ```bash
   docker compose up -d
   ```

4. Once the containers are running, **get the ID of the non-Postgres container** by running:

   ```bash
   docker container ls
   ```

5. **Exec into the non-DB container**:

   ```bash
   docker exec -it <container-id> sh
   ```

6. In the container command line, **run the following command to create the necessary tables**:

   ```bash
   psql postgresql://admin:admin@<postgres-container-id>:5432/mediacat -af mediacat.sql
   ```

7. To populate the DB and create an admin user, **run the following in the non-DB container**:

   ```bash
   python3 create_mediacat_db.py
   ```

## Accessing the Application

This is a demo application and will be running on `localhost:5000`. To log in to the application, use:

- **Username**: `admin`
- **Password**: `admin`

**NOTE**: The Docker image can be found here: [https://hub.docker.com/repository/docker/zstall/mediacat-flask-app/general](https://hub.docker.com/repository/docker/zstall/mediacat-flask-app/general)
