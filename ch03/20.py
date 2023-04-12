import json

def get_UKdata():
  f = open("jawiki-country.json", "r")
  lines = f.readlines()
  for line in lines:
    json_data = json.loads(line)
    if json_data["title"] == "イギリス":
      f.close()
      return json_data["text"]

data = get_UKdata()
print(data)
