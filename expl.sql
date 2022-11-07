-- Exploration queries
SELECT * FROM lemma WHERE ortografi = 'abnorm';

-- SELECTING LEMMAS
SELECT l.s_nr, l.ortografi, sl.s_nr, sl.origin
FROM lemma l
INNER JOIN superlemma sl
ON l.s_nr = sl.s_nr
WHERE l.ortografi = 'abnorm';

-- GLOBAL DEFINITIONS FOR A LEMMA
SELECT l.s_nr, l.ortografi, b.def, b.deft, b.typ
FROM betydelser b
INNER JOIN lemma l
ON l.s_nr = b.s_nr
WHERE l.ortografi = 'abnorm';

-- E
SELECT sl.s_nr, l.ortografi, u.*
FROM uttal u
INNER JOIN superlemma sl ON sl.s_nr = u.s_nr
INNER JOIN lemma l ON l.s_nr = sl.s_nr
WHERE l.ortografi = 'abnorm';

SELECT *
FROM betydelser
WHERE kc_nr = 410188;

SELECT * FROM etymologier WHERE x_nr = 100151;

-- WIP FINAL QUERYj
SELECT sl.s_nr,
  sl.ordklass as nature,
  l.ortografi as word,
  b.kc_nr,
  b.def as sense,
  b.deft as senseSecondary,
  b.typ,
  b.fkom,
  b.x_nr,
  e.fbel as ety_year,
  e.etymologi,
  GROUP_CONCAT(sy.sx_text SEPARATOR ';;') as examples
FROM superlemma sl
INNER JOIN lemma l
  ON l.s_nr = sl.s_nr
INNER JOIN betydelser b
  ON b.s_nr = sl.s_nr
INNER JOIN etymologier e
  ON e.x_nr = b.x_nr
INNER JOIN syntex sy
  ON sy.kc_nr = b.kc_nr
GROUP BY b.kc_nr
ORDER BY sl.s_nr ASC, b.kc_nr ASC, sy.sxorder;

SELECT sl.s_nr, sl.ordklass,
l.ortografi,
b.kc_nr as defId,
b.def as sense, b.deft as senseSecondary
FROM superlemma sl
INNER JOIN lemma l ON l.s_nr = sl.s_nr
INNER JOIN betydelser b ON b.s_nr = sl.s_nr
WHERE l.ortografi LIKE 'abn%'
GROUP BY sl.s_nr
LIMIT 50;


SELECT * FROM betydelser WHERE kc_nr = 410096;