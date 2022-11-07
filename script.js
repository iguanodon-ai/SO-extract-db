const fs = require("fs");
const knex = require("knex");

const db = knex({
  client: "mysql",
  connection: {
    host: "127.0.0.1",
    port: 3306,
    user: "root",
    password: "secret",
    database: "dictionary",
  },
});

function groupDefinitions(rows) {
  const grouped = rows.reduce((acc, curr) => {
    const { nature, word, sense, senseSecondary, ety_year, etymologi } = curr;
    const entry = {
      nature,
      sense,
      senseSecondary,
      year: ety_year,
      etymology: etymologi,
      examples: curr.examples ? curr.examples.split(";;") : "",
    };
    if (!acc.length) {
      return [{ key: word, entries: [entry] }];
    }
    if (acc.length && acc[acc.length - 1].key === word) {
      acc[acc.length - 1].entries.push(entry);
      return acc;
    }
    acc.push({ key: word, entries: [entry] });

    return acc;
  }, []);

  return grouped;
}

db.raw(
  "SELECT sl.s_nr, \
sl.ordklass as nature, \
l.ortografi as word, \
b.kc_nr, \
b.def as sense, \
b.deft as senseSecondary, \
b.typ, \
b.fkom, \
b.x_nr, \
e.fbel as ety_year, \
e.etymologi, \
GROUP_CONCAT(sy.sx_text SEPARATOR ';;') as examples \
FROM superlemma sl \
INNER JOIN lemma l \
ON l.s_nr = sl.s_nr \
INNER JOIN betydelser b \
ON b.s_nr = sl.s_nr \
INNER JOIN etymologier e \
ON e.x_nr = b.x_nr \
INNER JOIN syntex sy \
ON sy.kc_nr = b.kc_nr \
GROUP BY b.kc_nr \
ORDER BY sl.s_nr ASC, b.kc_nr ASC, sy.sxorder"
)
  .then((results) => {
    const [rows] = results;
    const grouped = groupDefinitions(rows);
    return fs.promises.writeFile("./entries.json", JSON.stringify(grouped));
  })
  .finally(() => console.log("end"));
