with open("sample.txt", "r") as src, open("copy.txt", "w") as dst:
 for line in src:
     dst.write(line)
