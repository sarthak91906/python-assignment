src = input()
dest = input()

f1 = open(src, "r")
lines = f1.readlines()
f1.close()

f2 = open(dest, "w")
for line in lines:
    if not line.strip().startswith("#"):
        f2.write(line)
f2.close()

print(open(src).read())
print(open(dest).read())