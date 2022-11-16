def dict_to_json(dictionary,jsonName):
    import json
    with open(jsonName, "w") as json_file:
        json.dump(dictionary, json_file, indent=4)

def json_to_dict(jsonName):
    import json
    with open(jsonName) as json_file:
        dictionary = json.load(json_file)

    return dictionary