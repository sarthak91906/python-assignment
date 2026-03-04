s = input("Enter a string: ")

vowels = "aeiouAEIOU"
v = 0
c = 0
sp = 0
l = 0

for ch in s:
    if ch in vowels:
        v += 1
    elif ch.isalpha():
        c += 1
    if ch == " ":
        sp += 1
    if ch.islower():
        l += 1

print("Number of Vowels:", v)
print("Number of Consonants:", c)
print("Number of Spaces:", sp)
print("Number of Lowercase Letters:", l)