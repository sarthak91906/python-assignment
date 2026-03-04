lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

for line in lines:
    print(line.upper())