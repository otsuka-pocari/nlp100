import re

s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = [re.sub(r"[^A-Za-z]", "", word) for word in s.split()]

answer = {}
extract_onechar_index_list = list(map(lambda x: x - 1, [1, 5, 6, 7, 8, 9, 15, 16, 19]))

for i in range(len(words)):
  if i in extract_onechar_index_list:
    answer[words[i][:1]] = i + 1
  else:
    answer[words[i][:2]] = i + 1
  
print(answer)
