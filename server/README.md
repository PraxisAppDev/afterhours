# Backend Setup

## Instructions
1. Install <a href="https://www.docker.com/products/docker-desktop/">Docker Desktop</a>

    This installs the `docker` and `docker-compose` commands

2. Start Docker Desktop
    - Just launch it

3. Configure environment variables
    - Locations
      > server/mongo.config.env

      > server/app/.env

4. Build and start containers

    - Default Mode
      >docker-compose up

    - Detached Mode
      >docker-compose up -d

5. Stop and remove containers

    >docker-compose down