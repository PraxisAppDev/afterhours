import os

command = "docker-compose -f ../docker-compose.yml --profile test up --build \
  --abort-on-container-exit --exit-code-from test && docker-compose -f \
  ../docker-compose.yml --profile test down"

os.system(command)