### String slicing
""" With slicing we can access substrings. It can get optional start and stop indices.
Syntex: string[start:end:step]
"""

s = '   hello   '
s = s[3:8]  # no crash if s[3:20]
print(s)
print()
a="water world"
print(a[1:9:3])
b="ThunderSoft"
print()
print(b[3:7:2])
print("\r")

####with string slicing we get the reverse string
string= "Hello my world"
print(string[::-1])