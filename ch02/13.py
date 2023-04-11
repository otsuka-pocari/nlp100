f1 = open("col1-python.txt", "r")
f2 = open("col2-python.txt", "r")
g = open("13-python.txt", "w")

f1_line_split = f1.read().split()
f2_line_split = f2.read().split()

for i in range(len(f1_line_split)):
  g.write(f1_line_split[i] + "\t" + f2_line_split[i] + "\n")

f1.close()
f2.close()
g.close()
