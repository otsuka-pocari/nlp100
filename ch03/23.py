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
sections_plain = re.findall(r"={2,}.+={2,}", data)

for section_plain in sections_plain:
  section_name = section_plain.replace("=", "")
  section_level = section_plain.count("=") // 2
  print("セクション名:{}\nレベル:{}".format(section_name, section_level))
