import json
import glob


for path in glob.iglob("out/*/*.json"):
    with open(path) as f:
        item: dict = json.load(f)

    changes = False
    print(path)
    if item["stac_version"] == "1.1.0":
        item["stac_version"] = "1.0.0"
        changes = True




    if changes:
        with open(path, "w") as f:
            json.dump(item, f, indent=2)