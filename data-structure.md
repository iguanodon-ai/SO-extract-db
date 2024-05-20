## Data structure of SO2021

This is the SO2021 dictionary stored in JSON. 

This is a list of dictionaries. Indeed, SO can have different different entries for the same surface form, so we can't use the lemma/headword as a key. We differentiate headwords with a key called `key`, an integer. You can inspect this by looking up the word _bot_: 
- there is a _bot_ (key == 1940) that means "straff som ut­går i pengar",
- a _bot_ (key == 37412) with two senses ("(religiös) handling varigenom ngn anses bli fri från skuld" + "medel för att avhjälpa brist eller felaktighet"),
- a _bot_ (key == 217078) from 2006 with only one sense: "datorprogram som simulerar mänskligt beteende"


The list contains 68671 dictionaries, one per dictionary entry. Each dictionary entry has several keys: `definitions` listing entries for that headword, `key` a unique ID (cf above), `nature` for the POS-tag, `word` for the headword.

 Below is an example: [svindel](https://svenska.se/so/?sok=svindel&pz=1). We explain the entry step by step, and in [the key section](#key) we provide a guide. In [remarks](#remarks) we provide a PoS-to-UD conversion scheme.

 The entry for `svindel` contains: 
 - the unique ID: 145357
 - the word: svindel
 - the part-of-speech (nature): "subst"
 - internal information for SO collaborators
 - the list of main senses. Each sense has its own dictionary, with:
    - possibly sub-senses,
    - a gloss,
    - possibly a sub gloss,
    - a list of example sentences (possibly none, possibly several),
    - a year  --- always a string and not an integer or a date, as sometimes the field contains a sentence (e.g.: "belagt sedan 2006")
 
A picture is worth a thousand words:

```python
[
     {
        "key": 145357,
        "word": "svindel",
        "nature": "subst.",
        "internal_SO_info": 1,
        "definitions": [
            {
                "gloss": "+yrsel som uppkommer vid vistelse på höga höjder",
                "sub_gloss": "",
                "sub_entries": [
                    {
                        "gloss": "äv. om likn. känsla som uppstått av annan orsak",
                        "sub_gloss": "",
                        "sub_entries": [],
                        "examples": [
                            "han kände svindel vid tanken på hur mycket pengar han hade ansvar för"
                        ],
                        "year": "1668"
                    }
                ],
                "examples": [
                    "hon fick svindel uppe i tornet"
                ],
                "year": "1668"
            },
            {
                "gloss": "(ekonomiskt) bedrägeri",
                "sub_gloss": "i större skala",
                "sub_entries": [],
                "examples": [],
                "year": "1879"
            }
        ]
    },
    {
        # entry for some other word
    },
    {
        # entry for some other word
    },

]

```
## Key

### `nature` (POS-tag)
They are both referring to a noun (`'nature': 'subst.'`, i.e. substantive). A list of possible natures is pasted below.

### `gloss` and `sub_gloss`
Sense definition (`gloss`), clarification of that sense definition (`sub_gloss`).

### `year` (year)
Time data available.

**NB**: 
1. This is a str
2. When the year ends in `00`, such as `1800`, this means "19th-Century" or "the years that started in 1800"

###  `examples` (examples)
A list of sentences/text using the word. This list can be empty, or contain one or more entries.

## Stats

- Number of words:  68671
- Number of senses:  87600
- Number of sub-senses:  18033
- Number of examples of main senses:  83974
- Number of examples of subsenses:  19610
- Number of examples (total):  103584
- Average number of senses per word:  1.276
- Average number of sub-senses per sense:  0.206
- Average number of examples per sense:  0.959
- Average number of examples per sub-sense:  1.087

## Bib

Allén, Sture (1981): The lemma-lexeme model of the Swedish Lexical Database. In: Ralph, Bo (ed.). Modersmålet i fäderneslandet. Ett urval uppsatser under fyrtio år av Sture Allén. Meijerbergs arkiv för svensk ordforskning 25. Göteborg 1999. https://gupea.ub.gu.se/bitstream/handle/2077/53653/gupea_2077_53653_1.pdf?sequence=1&isAllowed=y

## Remarks

Possible natures, their translation into English, and their meta [UD POS-tag](https://universaldependencies.org/u/pos/all.html) where available:

```python
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
