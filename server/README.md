# Backend Setup

## Instructions
1. Install <a href="https://www.docker.com/products/docker-desktop/">Docker Desktop</a>

    This installs the `docker` and `docker-compose` commands

2. Start Docker Desktop
    - Open the app like any other application

3. Configure environment variables
    - Locations
      > server/mongo.config.env

      > server/app/.env

4. Build and start containers
    - The docker-compose file currently has two profiles: `dev` and `test`
        - `dev` simply runs the server
        - `test` runs integration tests (at the moment)

    - To build and start `dev` containers
        - `dev` Default Mode
          >docker-compose --profile dev up --build

        - `dev` Detached Mode
          >docker-compose --profile dev up --build -d

    - To build and start `test` containers
        - `test` Default Mode
          >docker-compose --profile test up --build --abort-on-container-exit --exit-code-from test
        
        - `test` python3 script (in test directory)
          >python3 run_tests.py

5. For `dev` Only - View API Spec and Documentation

    - Type in the following address to see the Swagger UI in your browser
      >http://localhost:8001/docs#/

6. Stop and/or remove containers
    - `dev`
      >docker-compose --profile dev down
    - `test`
      >docker-compose --profile test down

## Dockerless Support

### Prerequisites
- You need to have <a href="https://www.mongodb.com/docs/manual/administration/install-community/">MongoDB Community Edition</a> installed
- Have bcrypt installed (will eventually move to environment.yml and use conda but for now this is the way around the limitations of requirements.txt)
- Replace ME_CONFIG_MONGODB_URL value to "mongodb://localhost:27017" in .env file

1. Run server
    - In the `server` directory, run the following
      >python3 dockerless.py

2. Close server
    - `CTRL-C`

For more details, check the `dockerless.py` file in the `server` directory