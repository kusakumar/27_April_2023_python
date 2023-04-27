""" strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)
syntex: string.strip(characters)

strip() method in Python removes or truncates the given characters from the beginning and the end of the original string.
strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)
"""

# Default method calling
string = '  xoxo love xoxo   '

# Leading and trailing whitespaces are removed
print(string.strip())
print()

txt = "     Hello world     "
x = txt.strip()
print("welcome to my", x, "and have great joye")

# strip() with combination of characters
# All <whitespace>,x,o,e characters in the left
# and right of string are removed
print(string.strip(' xoe'))
print()
# Argument doesn't contain space then No characters are removed.
print(string.strip('stx'))
print()
txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(" ,.grt")
print(x)

string = 'android is awesome'
print(string.strip('an'))
str1 = "Welcome to Great world!"
after_strip = str1.strip()
print(after_strip)

str2 = "Welcome to Great world!"
after_strip1 = str2.strip()
print(after_strip1)
print()
str1 = "****Welcome to Great world!****"
after_strip = str1.strip("*")
print(after_strip)

str2 = "Welcome to Great world!"
after_strip1 = str2.strip("99!")
print(after_strip1)
str3 = "Welcome to Great world!"
after_strip3 = str3.strip("to")
print(after_strip3)
print()

string = "  $$$$$  No. 1 Welcome to GREAT LEARNING!! No. 1 $$$  "
res = string.strip ( ' $No. 10 !' ) # store result into res variable
print ( " Given string is: ", string)
print ( " After removing the set of characters: ", res)
print()
str3 = ' 1 11 111 111 1111 Learn Python Tutorial 1111 111 11 1 '
str4 = str3. strip ( '1 ')
print (" \n  Given string is ", str3)
print (" Stripping 1 from both ends of the string using strip ('1') function ", str4)

print()

# define new string
str5 = '++++++Python Tutorial****** $$$$$'
print ("\n Given string is = ", str5)
# use strip function to remove the symbols from both ends
str6 = str5. strip ( ' $*+' )
print (" Stripping the ‘+’, ‘*’ and ‘$’ symbols on both sides of the string is = ", str6)