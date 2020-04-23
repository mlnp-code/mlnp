from glob import glob

for i in glob("*.md"):
    f = open(i, "r")
    content = f.readlines()
    f.close()

    g = open(i, "w")
    for j in content:
        g.write(j.replace("    |", "|"))
    g.close()

