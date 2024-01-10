**Documentation about data-structure is available in [data-structure.md](data-structure.md)**

# Usage

## If you have a node environment

`npm install` or `yarn install`

`npm run build` or `yarn build`

Create an `.env` file containing DB connection parameters (you can copy `env.sample` and edit the values)

`npm run start > entries.json` or `yarn start > entries.json`

## With Docker

`docker build -t so-db-extract:latest`

Create an `.env` file containing DB connection parameters (you can copy `env.sample` and edit the values)

`docker run --env-file <your-env-file> so-db-extract:latest > entries.json`

## Clean-up script

`python dedup_json.py`

Resulting JSON will be written in `./entries_clean.json`

NB: you might need to install the dependencies (`pip install -r requirements.txt`)
