f = open("popular-names.txt", "r")
g = open("14-python.txt",  "w")
lines = f.readlines()

N = int(input("N >= "))
for i in range(N):
  g.write(lines[i])

f.close()
g.close()
