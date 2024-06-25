import json

inputFile = "raw_data.json"
players = []

tags = {
    "#ffffff"  : "watched",
    "#ff3300"  : "cheating",
    "#33ff00"  : "innocent",
    "#ffff00"  : "suspicious",
    "#00ffff"  : "megascatterbomb",
}

with open(inputFile, "rb") as f:
    data = dict(json.load(f))

for k,v in data.items():
    colour = v["color"]["border"]
    tag = ""

    # ik theres an easier way todo this but i hate writing that way
    if colour in tags:
        tag = tags[colour]
    else:
        tag = "unknown"

    a = {
        "id"                : v["id"],
        "id3"               : v["id3"] ,
        "id1"               : v["id1"],
        "latest_name"       : v["label"],
        "previous_names"    : v["aliases"],
        "tag"               : tag
    }
    players.append(a)

with open("output.json", "w") as file:
    json.dump(players,file,indent=3)
    print(f"Finished, found: {len(players)} players")

