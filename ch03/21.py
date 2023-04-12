import json
import re

def get_UKdata():
  f = open("jawiki-country.json", "r")
  lines = f.readlines()
  for line in lines:
    json_data = json.loads(line)
    if json_data["title"] == "イギリス":
      f.close()
      return json_data["text"]

data = get_UKdata()
categories_plain = re.findall(r"\[\[Category:.+\]\]", data)

for category_plain in categories_plain:
  print(category_plain)
