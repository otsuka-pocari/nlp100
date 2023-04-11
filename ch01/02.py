texts = ["パトカー", "タクシー"]
answer = ""
for i in range(len(texts[0])):
  answer += texts[0][i] + texts[1][i]
print(answer)
