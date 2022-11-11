def dict_to_json(dictionaryName):
    import json
    with open("FCRModel.json", "w") as json_file:
        json.dump(dictionaryName, json_file, indent=4)

def json_to_dict():
    import json
    with open('FCRModel.json') as json_file:
        dictionary = json.load(json_file)

    return dictionary