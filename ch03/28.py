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

### 28. MediaWikiマークアップの除去

# 改行も含め、"{{基礎情報"から始まり"}}\n\n"で終わる部分を抽出するための正規表現
pattern_basic_info = re.compile(r"\{\{基礎情報([\s\S]+?)\}\}\n\n")
# 強調マークアップを除去する('', ''', '''''を除去する)ための正規表現
pattern_sub_emphasize = re.compile(r"('{2,5})(.+?)\1")
# ファイルリンクのマークアップを改修するための正規表現
pattern_sub_file = re.compile(r"\[\[ファイル:([\s\S]+?)(?:\|[\s\S]+?)*\]\]")
# 内部リンクのマークアップを除去するための正規表現
pattern_sub_internal_link = re.compile(r"\[\[([\s\S]+?)(?:\|[\s\S]+?)*\]\]")
# refタグやbrタグを消去するための正規表現
pattern_sub_tag = re.compile(r"(?:<ref>)?(?:</ref>)?(?:<br />)?(?:<ref[\s\S]+>?)?")
# {{lang|...}}系を改修するための正規表現
pattern_sub_lang = re.compile(r"\{\{lang\|(?:[\s\S]+?)([^\|]+)\}\}")
# 仮リンクを抽出するための正規表現
pattern_sub_tmp_link = re.compile(r"\{\{仮リンク\|([\s\S]+?)(?:\|[\s\S]+?)\}\}")
# その他{{と}}で囲まれた部分をスペースに変換するための正規表現
pattern_sub_curly_brackets = re.compile(r"\{\{(.+?)\}\}")
# :en: を削除するための正規表現
pattern_sub_en = re.compile(r"\:en\:")
# フィールド名と値の組を抽出するための正規表現
pattern_field_and_value = re.compile(r"\|(.+?)\s*=\s*([\s\S]+?)(?=\n\||\n\}\}\n\n)")

# イギリスに関する記事データ全部分を抽出する
data = get_UKdata()
# 改行も含め、"{{基礎情報"から始まり"}}\n\n"で終わる部分を抽出する
basic_info = pattern_basic_info.search(data).group()
# 強調マークアップを除去する('', ''', '''''を除去する)
basic_info = pattern_sub_emphasize.sub(r"\2", basic_info)
# ファイルリンクのマークアップを改修する
basic_info = pattern_sub_file.sub(r"\1", basic_info)
# 内部リンクのマークアップを除去する
basic_info = pattern_sub_internal_link.sub(r"\1", basic_info)
# refタグやbrタグを消去する
basic_info = pattern_sub_tag.sub(r'', basic_info)
# {{lang|...}}系を改修する
basic_info = pattern_sub_lang.sub(r"\1", basic_info)
# 仮リンクを抽出する
basic_info = pattern_sub_tmp_link.sub(r"\1", basic_info)
# その他{{と}}で囲まれた部分をスペースに変換する
basic_info = pattern_sub_curly_brackets.sub(r" ", basic_info)
# :en: を削除する
basic_info = pattern_sub_en.sub(r"", basic_info)
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
