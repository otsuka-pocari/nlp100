f = open("popular-names.txt", "r")
g = open("17-python.txt", "w")

lines = f.readlines()
col1 = [lines[i].split()[0] for i in range(len(lines))]
col1_set_sorted = sorted(list(set(col1)))
  
for i in range(len(col1_set_sorted)):
    g.write(col1_set_sorted[i] + "\n")
  
f.close()
g.close()
