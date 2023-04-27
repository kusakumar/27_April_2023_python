##isdigit
"""Returns True if all characters in the string are digits,
means isdigit() method returns True if all the characters are digits, otherwise False """
n= "Hello kusa, How are you doing"
m= "123456"
p="12.3456"
q="123 Helloworld4567"
r = '23455'
print(r.isdigit())
print(n.isdigit())
print(m.isdigit())
print(p.isdigit())
print(q.isdigit())
s1 = '²3455'
# subscript is a digit,Exponents, like ², are also considered to be a digit
print(s1.isdigit())
print()
s = '\u00B23455'
print(s.isdigit()) #Unicodes are difits
print()
s2 = '½'
print(s2.isdigit())
# fraction is not a digit

##strip()
print()
s = '   hello   '
s = s[3:8]
print(s.strip())
p= '   hello   '
p = p[1:20]  # no crash
print(p.strip())


##lstrip() and rstrip()
""" Return a copy of the string with leading characters removed. 
rtrip([chars]): Return a copy of the string with trailing characters removed. """

print('   hello   '.lstrip())
print()
print('   hello   '.rstrip())

###replace()
""" Return a copy of the string with all occurrences of substring old replaced by new
 Replaces all occurrences of a substring with another substring(Returns a string where a specified value is replaced with a specified value)
  Syntex: string.replace(oldvalue, newvalue, count)"""

txt = "I love watching movies"
x = txt.replace("movies", "comedy bits")
print(x)
print()

mystr = "Hello Python. Hello Java. Hello C++."
print(mystr.replace("Hello","Bye"))
print("\r")

#Replace all occurrence of the word "one":
txt = "one one was a race horse, two two was one too."
y = txt.replace("one", "three")
print(y)
print()

#Replace the two first occurrence of the word "one":
txt = "one one was a race horse, two two was one too."
z = txt.replace("one", "three", 2)
print(z)
print()
print(mystr.replace("Hello","Hell", 2))

###lower()
""" Converts a string into lower case
Syntax: string.lower()
Parameters: The lower() method doesn’t take any parameters.
Returns: Returns a lowercase string of the given string
"""
i= "PyTHon 457 heLLO, Are YOU LearninG"
print(i.lower())
print()
###Compersion of strings using lower() method
text1="Hello Where are You"
text2="hELLO wHERE Are yOU"
#text2="Hello, Where are You Going"
if(text1.lower() == text2.lower()):
    print("Strings are same")
else:
    print("Strings are not same")

#### upper()
""" Converts all lowercase characters in a string into uppercase
Syntax: string.upper()
Parameters: The upper() method doesn’t take any parameters. 
Returns: returns an uppercased string of the given string. """
print("\r")
text1="Hello Where are You"
text2="hELLO wHERE Are yOU"
#text2="Hello, Where are You Going"
if(text1.upper() == text2.upper()):
    print("Strings are same")
else:
    print("Strings are not same")

####startswitch()
"""" startswith() method returns True if a string starts with the specified prefix (string). 
If not, it returns False.
Syntax: str.startswith(prefix, start, end)
prefix: prefix ix nothing but a string that needs to be checked.
start: Starting position where prefix is needed to be checked within the string.
end: Ending position where prefix is needed to be checked within the string.
 """
##Python String startswith() Method Without start and end Parameters
text = "All telugu movies are my favourite ones"
x = text.startswith("all")
print(x)
print(text.startswith("All"))
print()
mystr1 = "Hello Python. Hello Java. Hello C++."
print(mystr1.startswith("Hello"))
print(mystr1.startswith("Bye"))
print()
##Python String startswith() Method With start and end Parameters

print("\r")
print(mystr1.startswith("Python",6))
print(mystr1.startswith("python",6))
print(mystr1.startswith("Python.",6,13))
print()
print("\r")
####startswith() method will return True if the string starts with any of the item in the tuple
string = "apple"
res = string.startswith(('a', 'e', 'i', 'o', 'u'))
print(res)
string = "mango"
res = string.startswith(('a', 'e', 'i', 'o', 'u'))
print(res)

####endswitch
""" 
endswith() method returns True if a string ends with the given suffix, otherwise returns False
Syntax: str.endswith(suffix, start, end)

Parameters: 
suffix: Suffix is nothing but a string that needs to be checked. 
start: Starting position from where suffix is needed to be checked within the string. 
end: Ending position + 1 from where suffix is needed to be checked within the string.
Return: ReturnsTrue if the string ends with the given suffix otherwise return False.
"""
mychrs = "Python"
print(mychrs.endswith("y"))
print(mychrs.endswith("hon"))
print()

Str="Hi,Shall we go out"
print(Str.endswith("Hi"))
print(Str.endswith("out"))
print(Str.endswith("go out"))
print(Str.endswith("Out"))
print()