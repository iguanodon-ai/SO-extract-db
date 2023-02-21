# Usage

## Prepare database dump

Dump can be put in `./dbfiles/<filename>.sql`. Make sure the SQL starts with `create database dictionary;`.
You may want to modify `docker-compose.yml` volumes block to reflect your dump filename

## Database setup

Run the database with docker :

```
docker compose up
```

Depending on the dump size, this may take some time before the container is ready

## JS dependencies

You will need to have a working installation of nodejs (latest LTS preferably).

You can install deps with `npm` or `yarn`.

```
npm install
```

OR

```
yarn install
```

## Run the script

`node script.js`

Resulting JSON will be written in `./entries.json`

## Clean-up script

`python dedup_json.py`

Resulting JSON will be written in `./entries_clean.json`

NB: you might need to install the dependencies (`pip install -r requirements.txt`)
