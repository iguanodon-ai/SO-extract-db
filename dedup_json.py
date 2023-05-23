import json
from pprint import pprint
import sys
from tqdm import tqdm
import re


def try_set(dic):
    #pprint(dic)
    try:
        dic["examples"] =  list(set(dic["examples"]))
        return dic
    except:
        return dic
        

def dedup(d):
    d2 = []
    for i in tqdm(d):
        dico = {"entries": []}
        dico["key"] = i["key"]
        
        for x in i["entries"]:
            dico["entries"].append(try_set(x))
        d2.append(dico)
            
    return d2

def clean_dates(d):
    for i, v in enumerate(d):
        for i2, entry in enumerate(v["entries"]):
            dates = re.findall("\d{4}", entry["year"])
            d[i]["entries"][i2]["year"] = [int(date) for date in dates]
    return d

def list_to_dict(d):
    d4 = {}
    for i in d:
        w = i["key"]
        i.pop("key")
        d4[w] = i
    return d4

with open("entries.json") as f:
    d = json.load(f)
    
d2 = dedup(d)
d3 = clean_dates(d2)
d4 = list_to_dict(d3)

with open("entries_clean.json", "w") as f:
    json.dump(d4, f, indent=4, ensure_ascii=False)
print("Dedup JSON saved at entries_clean.json")
