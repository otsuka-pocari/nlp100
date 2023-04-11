f = open("popular-names.txt", "r")
lines = f.readlines()

N = int(input("N => "))
g = [open("16-python-%2d.txt" % i, "w") for i in range(N)]
number_of_lines_per_a_file = len(lines) // N

index = 0
for i in range(N):
  for j in range(number_of_lines_per_a_file):
    g[i].write(lines[index])
    index += 1

while index < len(lines):
  g[-1].write(lines[index])
  index += 1

f.close()
for i in range(N):
  g[i].close()
