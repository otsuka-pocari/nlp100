import random

random.seed(0)

original_sentence = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

modified_words = []
for original_word in original_sentence.split():
  if len(original_word) > 4:
    middle_part = list(original_word[1:-1])
    random.shuffle(middle_part)
    modified_words.append(original_word[0] + "".join(middle_part) + original_word[-1])
  else:
    modified_words.append(original_word)
modified_sentence = " ".join(modified_words)

print("--- Original Sentence ---")
print(original_sentence)
print("--- Typoglycemia ---")
print(modified_sentence)
