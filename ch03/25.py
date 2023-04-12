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

# 改行も含め、"{{基礎情報"から始まり"}}\n\n"で終わる部分を抽出するための正規表現
pattern_basic_info = re.compile(r"\{\{基礎情報([\s\S]+?)\}\}\n\n")
# フィールド名と値の組を抽出するための正規表現
pattern_field_and_value = re.compile(r"\|(.+?)\s*=\s*([\s\S]+?)(?=\n\||\n\}\}\n\n)")

# イギリスに関する記事データ全部分を抽出する
data = get_UKdata()
# 改行も含め、'{{基礎情報'から始まり'}}\n\n'で終わる部分を抽出する
basic_info = pattern_basic_info.search(data).group()
# フィールド名と値の組を抽出する
field_name_value_pairs = pattern_field_and_value.findall(basic_info)

# フィールド名と値の辞書を作成
field_name_value_dict = {}
for field_name, field_value in field_name_value_pairs:
  field_name_value_dict[field_name] = field_value

# フィールド名と値の辞書の内容を確認
for field_name, field_value in field_name_value_dict.items():
  print("-" * 50)
  print("[フィールド名]\n{}".format(field_name))
  print("[値]\n{}".format(field_value))
