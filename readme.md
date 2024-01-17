**Documentation about data-structure is available in [data-structure.md](data-structure.md)**

# Usage

## If you have a node environment

`npm install` or `yarn install`

`npm run build` or `yarn build`

Create an `.env` file containing DB connection parameters (you can copy `env.sample` and edit the values)

`npm run start > entries.json` or `yarn start > entries.json`

## With Docker

`docker build -t so-db-extract:latest .`

Create an `.env` file containing DB connection parameters (you can copy `env.sample` and edit the values)

`docker compose up`

This will spin up mariadb. The first time you run this, it will ingest the SQL. Check logs to see it's correctly finished doing so, otherwise the command below will not work. If you need to kill the volume and start again, do `docker compose down -v`, delete the volume on this, and start again. 

`docker run --env-file <your-env-file> so-db-extract:latest > entries.json`

You might need to clean the first lines of the json.

## Clean-up script

`python dedup_json.py`

Resulting JSON will be written in `./entries_clean_nodraft.json`

NB: you might need to install the dependencies (`pip install -r requirements.txt`)
