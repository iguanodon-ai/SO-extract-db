import { config } from "dotenv";
import { Kysely, MysqlDialect, sql } from "kysely";
import { createPool } from "mysql2";
import { Database, Entry } from "./types";

config();

const dialect = new MysqlDialect({
  pool: createPool({
    database: process.env.DB_NAME || "dictionary",
    host: process.env.DB_HOST || "127.0.0.1",
    port: Number(process.env.DB_PORT) || 3306,
    user: process.env.DB_USER || "root",
    password: process.env.DB_PASSWORD || "secret",
    connectionLimit: 1,
  }),
});

const db = new Kysely<Database>({ dialect });

async function parseEntries() {
  const data = await db
    .selectFrom("superlemma as sl")
    .innerJoin("lemma as l", "l.s_nr", "sl.s_nr")
    .innerJoin("betydelser as b", "b.s_nr", "sl.s_nr")
    .innerJoin("etymologier as e", "e.x_nr", "b.x_nr")
    .leftJoin("syntex as sy", "b.kc_nr", "sy.kc_nr")
    .where("l.wtype", "=", "lemma")
    // .where("l.ortografi", "in", ["svindel", "fuling", "bot"])
    .groupBy("b.kc_nr")
    .orderBy(["sl.s_nr asc", "b.x_nr asc", "b.kcorder asc"])
    .select([
      "sl.s_nr",
      "sl.ordklass",
      "sl.typ",
      "b.x_nr",
      "l.wtype",
      "l.origin",
      "l.ortografi",
      "b.def",
      "b.deft",
      "b.typ",
      "e.fbel",
      sql<string>`GROUP_CONCAT(sy.sx_text SEPARATOR ';;')`.as("examples"),
    ])
    .execute();

  return data.reduce((entries: Entry[], curr) => {
    const entry = entries.find((e) => e.key === curr.s_nr);
    if (!entry) {
      const newEntry: Entry = {
        key: curr.s_nr,
        word: curr.ortografi,
        nature: curr.ordklass,
        definitions: [
          {
            description: curr.def,
            subtitle: curr.deft,
            subDefinitions: [],
            examples: curr.examples ? curr.examples.split(";;") : [],
            year: curr.fbel,
          },
        ],
      };
      entries.push(newEntry);
    } else {
      if (!curr.def?.length && curr.typ) {
        entry.definitions[0].subDefinitions.push({
          description: curr.typ,
          subtitle: curr.deft,
          subDefinitions: [],
          examples: curr.examples ? curr.examples.split(";;") : [],
          year: curr.fbel,
        });
      } else if (curr.def?.length) {
        entry.definitions.push({
          description: curr.def,
          subtitle: curr.deft,
          subDefinitions: [],
          examples: curr.examples ? curr.examples.split(";;") : [],
          year: curr.fbel,
        });
      }
    }

    return entries;
  }, []);
}

function parseRows(data: any[]) {}

(async function () {
  const entries = await parseEntries();
  console.log(JSON.stringify(entries));
  return db.destroy();
})();
