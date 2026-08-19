"""Extract the SO2021 dictionary from a MariaDB/MySQL database into JSON.

Python port of the original TypeScript extractor (src/index.ts). It runs a
single join query across the superlemma/lemma/betydelser/etymologier/syntex
tables and reshapes the flat rows into nested dictionary entries.

The emitted JSON keys (`description`, `subtitle`, `subDefinitions`) match the
original TypeScript output so that `dedup_json.py` can rename them unchanged.
"""

import json
import os
import sys

import pymysql
from dotenv import load_dotenv
from tqdm import tqdm

QUERY = """
SELECT
    sl.s_nr,
    sl.ordklass,
    sl.typ,
    b.x_nr,
    l.wtype,
    l.origin,
    l.ortografi,
    l.lm_sabob,
    b.def,
    b.deft,
    b.typ,
    e.fbel,
    GROUP_CONCAT(sy.sx_text SEPARATOR ';;') AS examples
FROM superlemma AS sl
INNER JOIN lemma AS l       ON l.s_nr = sl.s_nr
INNER JOIN betydelser AS b  ON b.s_nr = sl.s_nr
INNER JOIN etymologier AS e ON e.x_nr = b.x_nr
LEFT JOIN  syntex AS sy      ON b.kc_nr = sy.kc_nr
WHERE l.wtype = 'lemma'
GROUP BY b.kc_nr
ORDER BY sl.s_nr ASC, b.x_nr ASC, b.kcorder ASC
"""


def get_connection():
    """Open a MySQL/MariaDB connection using DB_* environment variables."""
    return pymysql.connect(
        host=os.environ.get("DB_HOST", "127.0.0.1"),
        port=int(os.environ.get("DB_PORT", "3306")),
        user=os.environ.get("DB_USER", "root"),
        password=os.environ.get("DB_PASSWORD", "secret"),
        database=os.environ.get("DB_NAME", "dictionary"),
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )


def split_examples(value):
    """Split a GROUP_CONCAT examples string on ';;', or return an empty list."""
    return value.split(";;") if value else []


def parse_entries(rows):
    """Reshape flat DB rows into nested dictionary entries.

    Mirrors the reduce() in the original src/index.ts, including the special
    case where an existing entry has an empty `def` but a non-empty `typ`,
    which becomes a sub-definition.
    """
    entries = []
    by_key = {}

    for row in tqdm(rows, desc="Building entries", unit="row", file=sys.stderr):
        key = row["s_nr"]
        entry = by_key.get(key)

        if entry is None:
            entry = {
                "key": row["s_nr"],
                "word": row["ortografi"],
                "nature": row["ordklass"],
                "internal_SO_info": row["lm_sabob"],
                "definitions": [
                    {
                        "description": row["def"],
                        "subtitle": row["deft"],
                        "subDefinitions": [],
                        "examples": split_examples(row["examples"]),
                        "year": row["fbel"],
                    }
                ],
            }
            by_key[key] = entry
            entries.append(entry)
        else:
            if not row["def"] and row["typ"]:
                entry["definitions"][0]["subDefinitions"].append(
                    {
                        "description": row["typ"],
                        "subtitle": row["deft"],
                        "subDefinitions": [],
                        "examples": split_examples(row["examples"]),
                        "year": row["fbel"],
                    }
                )
            elif row["def"]:
                entry["definitions"].append(
                    {
                        "description": row["def"],
                        "subtitle": row["deft"],
                        "subDefinitions": [],
                        "examples": split_examples(row["examples"]),
                        "year": row["fbel"],
                    }
                )

    return entries


def main():
    load_dotenv()

    output_path = sys.argv[1] if len(sys.argv) > 1 else os.environ.get(
        "OUTPUT", "entries.json"
    )

    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(QUERY)
            rows = cursor.fetchall()
    finally:
        connection.close()

    entries = parse_entries(rows)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False)

    print(f"Wrote {len(entries)} entries to {output_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
