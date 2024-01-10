## Data structure of SO2021

This is the SO2021 dictionary stored in JSON. 

Below information is using python, but json is json. 

This is a list, as SO follows the lemma-lexeme model (Allén 1981) which means we can have several different entries for a specific lemma. You can inspect this by looking up the word `bot`, for example.

The list contains 68671 dictionaries, one per dictionary entry. Each dictionary entry has several keys: `definitions` listing entries for that headword, `key` a unique ID (cf above), `nature` for the POS-tag, `word` for the headword.

 Below are two examples: [fuling](https://svenska.se/so/?sok=fuling&pz=1) has one main entry and two sub-entry, one of them has an example sentence. [svindel](https://svenska.se/so/?sok=svindel&pz=1) has two main entries and one of those has a sub-entry. There is an example for that main sense, and another example for its sub-sense. 


```python
{'definitions': [{'examples': [],
                  'gloss': 'person (eller djur) med föga tilltalande yttre',
                  'sub_entries': [{'examples': [],
                                   'gloss': 'ofta bildligt om lömsk el. elak '
                                            'person',
                                   'sub_entries': [],
                                   'sub_gloss': '',
                                   'year': '1831'},
                                  {'examples': ['din lille fuling, vad har du '
                                                'nu gjort?'],
                                   'gloss': 'äv. skämts. el. smeksamt',
                                   'sub_entries': [],
                                   'sub_gloss': '',
                                   'year': '1831'}],
                  'sub_gloss': '',
                  'year': '1831'}],
 'key': 53284,
 'nature': 'subst.',
 'word': 'fuling'}


{'definitions': [{'examples': ['hon fick svindel uppe i tornet'],
                  'gloss': '+yrsel som uppkommer vid vistelse på höga höjder',
                  'sub_entries': [{'examples': ['han kände svindel vid tanken '
                                                'på hur mycket pengar han hade '
                                                'ansvar för'],
                                   'gloss': 'äv. om likn. känsla som uppstått '
                                            'av annan orsak',
                                   'sub_entries': [],
                                   'sub_gloss': '',
                                   'year': '1668'}],
                  'sub_gloss': '',
                  'year': '1668'},
                 {'examples': [],
                  'gloss': '(ekonomiskt) bedrägeri',
                  'sub_entries': [],
                  'sub_gloss': 'i större skala',
                  'year': '1879'}],
 'key': 145357,
 'nature': 'subst.',
 'word': 'svindel'}

```
## Key

### `nature` (POS-tag)
`drog` here above has two entries. They are both referring to a noun (`'nature': 'subst.'`, i.e. substantive). A list of possible natures is pasted below.

### `gloss` and `sub_gloss`
The first one has a sense definition (`gloss`) as well as a clarification of that sense definition (`sub_gloss`).

### `year` (year)
Time data available.

**NB**: 
1. This is an str
2. When the year ends in `00`, such as `1800`, this means "19th-Century" or "the years that started in 1800"

###  `examples` (examples)
A list of sentences/text using the word. This list can be empty, or contain one or more entries.


## Bib

Allén, Sture (1981): The lemma-lexeme model of the Swedish Lexical Database. In: Ralph, Bo (ed.). Modersmålet i fäderneslandet. Ett urval uppsatser under fyrtio år av Sture Allén. Meijerbergs arkiv för svensk ordforskning 25. Göteborg 1999. (https://gupea.ub.gu.se/bitstream/handle/2077/53653/gupea_2077_53653_1.pdf?sequence=1&isAllowed=y)

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