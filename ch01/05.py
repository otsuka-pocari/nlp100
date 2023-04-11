import re

def make_word_ngram(sentence, n):
  words = [re.sub(r"[^A-Za-z]", "", word) for word in sentence.split()]
  return [words[i: i + n] for i in range(len(words) - (n - 1))]

def make_character_ngram(sentence, n):
  return [sentence[i: i + n] for i in range(len(sentence) - (n - 1))]

text = "I am an NLPer"
n = 2

# make Word Bi-gram
word_ngram = make_word_ngram(text, n)
print("Word N-gram (N = {0}): {1}".format(n, word_ngram))

# make Character Bi-gram
character_ngram = make_character_ngram(text, n)
print("Character N-gram (N = {0}): {1}".format(n, character_ngram))
