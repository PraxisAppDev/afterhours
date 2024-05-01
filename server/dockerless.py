import os
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--reset', default=False, action='store_true')
args = parser.parse_args()

if args.reset:
  os.system("rm -rf testdb")

if not os.path.exists('./testdb'):
  os.system("mkdir testdb")

mongo = "mongod --dbpath testdb"
fastapi = "uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload"

with open("testdb/logs", "w") as outfile:
  ps = subprocess.Popen(mongo.split(), stdout=outfile)
  os.system(fastapi)
  ps.wait()
  ps.terminate()
