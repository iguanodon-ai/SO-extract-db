import json
from pprint import pprint
import sys
from tqdm import tqdm


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

with open("entries.json") as f:
    d = json.load(f)
    
d2 = dedup(d)
with open("entries_clean.json", "w") as f:
    json.dump(d2, f, indent=4, ensure_ascii=False)
print("Dedup JSON saved at entries_clean.json")
