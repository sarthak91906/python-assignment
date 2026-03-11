f1 = open(input(), "r")
data = f1.read()
f1.close()

f2 = open(input(), "w")
f2.write(data.upper())
f2.close()