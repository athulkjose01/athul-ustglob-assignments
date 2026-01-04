word = "Python"
line_no = 0
with open("sample.txt", "r") as f:
     for line in f:
         line_no += 1
         if word.lower() in line.lower():
            print(f"Found in line {line_no}: {line.strip()}")
