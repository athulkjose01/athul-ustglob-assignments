lines = words = chars = 0
with open("sample.txt", "r") as f:
 for line in f:
     lines += 1
     words += len(line.split())
     chars += len(line)
print("Lines:", lines)
print("Words:", words)
print("Characters:", chars)
