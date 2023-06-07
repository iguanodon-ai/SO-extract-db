## Data structure of SO2021

This is the SO2021 dictionary stored in JSON. 

Below information is using python, but json is json. 

```python
>>> import json
>>> with open("entries_clean.json") as f:
>>>     l = json.load(f)
>>> print(len(l))
41597
```

This is a list, as SO follows the lemma-lexeme model (Allén 1981) which means we can have several different entries for a specific lemma. You can inspect this by looking up the word `bot`, for example.

The list contains 51597 dictionaries, one per dictionary entry. Each dictionary entry has two keys: `entries` and `key`. The `key` is a string, the lemma at hand, while `entries` represent different entries for that specific key.

 A code excerpt is worth a thousand words:


```python
>>> l[6465]
    {
        "entries": [
            {
                "nature": "subst.",
                "sense": "narkotiskt medel",
                "senseSecondary": "särsk. när det används i annat syfte än medicinskt",
                "year": [
                    1721
                ],
                "etymology": "av fra. *drogue =; ev. av lågty. *droge- 'torr' i *droge-fate 'torra fat' (*droge- har felaktigt uppfattats som innehållet i faten)",
                "examples": [
                    "tunga droger",
                    "det är förbjudet att använda droger för att höja prestationsförmågan inom idrotten",
                    "hasch, morfin och andra droger"
                ]
            },
            {
                "nature": "subst.",
                "sense": "",
                "senseSecondary": "",
                "year": [
                    1721
                ],
                "etymology": "av fra. *drogue =; ev. av lågty. *droge- 'torr' i *droge-fate 'torra fat' (*droge- har felaktigt uppfattats som innehållet i faten)",
                "examples": [
                    "på sjukhuset behandlades hon med drogerna haloperidol och triftazin"
                ]
            }
        ],
        "key": "drog"
    }
```
## Key

### `nature` (POS-tag)
`drog` here above has two entries. They are both referring to a noun (`'nature': 'subst.'`, i.e. substantive). A list of possible natures is pasted below.

### `sense` and `senseSecondary` (senses)
The first one has a sense (`sense`) as well as a clarification of that sense (`senseSecondary`) -- in this case the sense is "a narcotic agent", and the clarification means "specific, used for purposes other than medicinal"

### `year` (year)
They both share the same year. 

**NB**: 
1. This is a list of ints, there might be several dates
2. When the year ends in `00`, such as `1800`, this means "19th-Century" or "the years that started in 1800"

###  `etymology` (etymology)
The etymology of the word.

###  `examples` (examples)
A list of sentences/text using the word. This list can be empty, or contain one or more entries.


## Bib

Allén, Sture (1981): The lemma-lexeme model of the Swedish Lexical Database. In: Ralph, Bo (ed.). Modersmålet i fäderneslandet. Ett urval uppsatser under fyrtio år av Sture Allén. Meijerbergs arkiv för svensk ordforskning 25. Göteborg 1999. (https://gupea.ub.gu.se/bitstream/handle/2077/53653/gupea_2077_53653_1.pdf?sequence=1&isAllowed=y)

## Remarks

Possible natures, their translation into English, and their meta [UD POS-tag](https://universaldependencies.org/u/pos/all.html) where available:
```
{
 'adj.' : ["adjective", "ADJ"],
 'adj. komp.': ["comparative adjective", "ADJ"],
 'adj. superl.': ["superlative adjective", "ADJ"],
 'adjektiviskt förled': ["adjectival prefix", "PART"],
 'adjektiviskt slutled': ["adjectival suffix", "PART"],
 'adv.': ["adverb", "ADV"],
 'artikel': ["article", "DET"],
 'förled': ["prefix", "PART"],
 'infinitivmärke': ["infinitive mark", "VERB"],
 'interj.': ["interjection", "INTJ"],
 'konj.': ["coordinating conjunction", "CCONJ"],
 'prep.': ["preposition", "ADP"],
 'pron.': ["pronoun", "PRON"],
 'räkn.': ["numeral", "NUM"],
 'subj.': ["subordinating conjunction", "SCONJ"],
 'subst.': ["substantive", "NOUN"],
 'substantiverat adj.': ["substantival adjective", "NOUN"],
 'substantiviskt slutled': ["substantival suffix", "NOUN"],
 'verb': ["infinitive mark", "VERB"]
 }
 ```