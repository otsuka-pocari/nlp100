def make_character_ngram(sentence, n):
  return [sentence[i: i + n] for i in range(len(sentence) - (n - 1))]

X = set(make_character_ngram("paraparaparadise", 2))
Y = set(make_character_ngram("paragraph", 2))

print("X => {0}".format(list(X)))
print("Y => {0}".format(list(Y)))
print("Union => {0}".format(X | Y))
print("Intersection => {0}".format(X & Y))
print("Does set X|Y contains 'se'? => {0}".format({"se"} <= (X | Y)))
