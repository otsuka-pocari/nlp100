f = open("popular-names.txt", "r")
g = open("18-python.txt", "w")

lines = f.read().split("\n")[:-1]
lines_and_values = []
for i in range(len(lines)):
    lines_and_values.append([lines[i], int(lines[i].split()[2])])
  
lines_and_values.sort(key=lambda x:x[1])
lines_and_values.reverse()
  
for i in range(len(lines_and_values)):
    g.write(lines_and_values[i][0] + "\n")
  
f.close()
g.close()
