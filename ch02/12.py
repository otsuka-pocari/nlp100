f = open("popular-names.txt", "r")
g1 = open("col1-python.txt", "w")
g2 = open("col2-python.txt", "w")
lines = f.readlines()

for line in lines:
  line_split = line.split()
  g1.write(line_split[0] + "\n")
  g2.write(line_split[1] + "\n")

f.close()
g1.close()
g2.close()
