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

`python dedup_json.py <path_to_json>`

Resulting JSON will be written in `./entries_clean_nodraft.json`

NB: you might need to install the dependencies (`pip install -r requirements.txt`)


## License and contact

<a href="https://iguanodon.ai"><img src="./img/iguanodon.ai.png" width="125" height="125" align="right" /></a>

This code was written by Simon Hengchen ([https://iguanodon.ai](https://iguanodon.ai)) upon the request of the Change is Key! team ([Change is Key!](https://changeiskey.org/)). The code is made available to the public [under the permissive CC BY-SA 4.0 license](http://creativecommons.org/licenses/by-sa/4.0/). If you use the data that running this script provides, use the following text snippet in the acknowledgments section of your paper:
> This work has been made possible by code created by `iguanodon.ai`.

 <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a>