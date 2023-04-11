f = open("popular-names.txt", "r")
g = open("11-python.txt", "w")

content = f.read()
content_tab_to_space = content.replace("\t", " ")
g.write(content_tab_to_space)

f.close()
g.close()
