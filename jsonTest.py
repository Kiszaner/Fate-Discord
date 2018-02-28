import json
import os.path

# data = {"Characters": [{"PC": [{"ID": "Jotas", "Name": "Waldrich", "Genre": "Male", "Species": "Human"},
#                                {"ID": "Jose", "Name": "Umgi'Got", "Genre": "Female", "Species": "Dwarf"}]},
#                        {"NPC": [{"ID": "Malo1", "Name": "Bobo", "Genre": "Male", "Species": "Human"},
#                                 {"ID": "Malo2", "Name": "Tonto", "Genre": "Male", "Species": "Human"}]}
#                        ]
#         }

JSON_FILE_NAME = "characters_test.json"
defaultData = {"Characters": [{"PC": []}, {"NPC": []}]}


def checkFile():
    if not os.path.isfile(JSON_FILE_NAME):
        print("File didn't exist, creating...")
        with open("characters_test.json", "w") as f:
            json.dump(defaultData, f, indent=4)
    else:
        print("File already exists")


def loadJSONFromFile(fname):
    with open(fname) as f:
        return json.load(f)


def writeToJSONFile(data, fname):
    with open(fname, "w") as f:
        json.dump(data, f, indent=4)


def createCharacter(id, name, genre, species):
    return {"ID": id, "Name": name, "Genre": genre, "Species": species}


def insertCharacter(is_npc, id, name, genre, species):
    checkFile()
    data = loadJSONFromFile(JSON_FILE_NAME)
    if is_npc:
        index = 1
        char_type = "NPC"
    else:
        index = 0
        char_type = "PC"
    new_char = createCharacter(id, name, genre, species)
    if new_char in data["Characters"][index][char_type]:
        print("Character already exists")
    else:
        print("Character didn't exist, adding...")
        data["Characters"][index][char_type].append(new_char)
        writeToJSONFile(data, JSON_FILE_NAME)


insertCharacter(False, "Jotas", "Waldrich", "Male", "Human")
insertCharacter(False, "Jose", "Umgi'Got", "Female", "Dwarf")
insertCharacter(False, "Mede", "Lo'Gosh", "Male", "Semi-Ork")
insertCharacter(False, "Cas", "Igni Rerik", "Male", "Draken")
insertCharacter(True, "Heber1", "Malo1", "Male", "Human")
insertCharacter(True, "Heber2", "Malo2", "Female", "Ork")
insertCharacter(True, "Heber3", "Malo3", "Male", "Birdman")
