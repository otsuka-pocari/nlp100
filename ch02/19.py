f = open("popular-names.txt", "r")
g = open("19-python.txt", "w")

lines = f.read().split("\n")[:-1]
col1 = [lines[i].split()[0] for i in range(len(lines))]

col1_counter = {}
for value in col1:
    if value in col1_counter.keys():
        col1_counter[value] += 1
    else:
        col1_counter[value] = 1
  
col1_freq_list = []
for value, freq in col1_counter.items():
    col1_freq_list.append([freq, value])
  
col1_freq_sorted = sorted(col1_freq_list, key=lambda x:x[0], reverse=True)
for col1_freq_data in col1_freq_sorted:
    g.write(("%7d" % col1_freq_data[0]) + "\t" + col1_freq_data[1] + "\n")
  
f.close()
g.close()

