import re

text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words = [re.sub(r"[^A-Za-z]", "", word) for word in text.split()]
answer = [0 for _ in range(len(words))]
for i in range(len(words)):
  answer[i] = len(words[i])
print("words: {0}".format(words))
print("answer: {0}".format(answer))
