from os.path import exists

import yaml

# Build the index file with Jinja2
with open("links.yaml", "r", encoding="utf8") as links_file:
    data = yaml.load(links_file, Loader=yaml.CLoader)

for category_name in data:
    for link in data[category_name]:
        for key in ["name", "description", "img", "url"]:
            if key not in link:
                raise KeyError(f"Missing key {key} for {link['name']}")
        if not exists("src/assets/icons/" + link["img"]):
            raise ValueError(f"Inexistant asset {link['img']} for {link['name']}")