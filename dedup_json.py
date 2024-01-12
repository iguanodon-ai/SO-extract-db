import json
from pprint import pprint

def rename_keys_dict(dictionary, key_map):
    """
    Recursive function to rename dictionary keys based on a key_map object.
    
    Args:
        dictionary (dict): The dictionary to rename keys.
        key_map (dict): The key_map object that maps old keys to new keys.
        
    Returns:
        dict: The dictionary with renamed keys.
    """
    renamed_dict = {}
    try:
        for key, value in dictionary.items():
            #print(key)
            if key in key_map:
                new_key = key_map[key]
                #print(key, new_key)
            else:
                new_key = key
            if isinstance(value, list):
                new_l = []
                for i in value:
                    i = rename_keys_dict(i, key_map)
                    new_l.append(i)
                value = new_l
                

                renamed_dict[new_key] = value
            else:
                renamed_dict[new_key] = value
    except:
        return dictionary
    return renamed_dict

key_mapping = {
    "description" : "gloss",
    "subDefinitions" : "sub_entries",
    "subtitle": "sub_gloss"
}

with open("entries.json") as f:
    data = json.load(f)
    
y = [rename_keys_dict(dic, key_mapping) for dic in data]

with open("entries_clean.json", "w") as f:
    json.dump(y, f, indent=4, ensure_ascii=False)
print("Dedup JSON saved at entries_clean.json")
