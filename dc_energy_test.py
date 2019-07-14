### all test were run with python version 2.7

### imports urllib2 to grab site source code and re to handle regular expressions in python(to parse source code)
import urllib2
import re

### opens the site as a str object
our_site = urllib2.urlopen("https://www.usinflationcalculator.com/inflation/").read()

### uncomment to print the object and it's type
# print(our_site)
# print(type(our_site))

### this searches for the historic inflation rates(since I know what it is already my regular expression just looks for
### the strings surrounding it.  This could instead be written to find a variety of possible patterns, but Im not doing
### that here.  I would use ?(optional) and | (or) and some combination of strings and parenthesis, etc.
### also in this case it will be an array containing a single item, but it could be more in which case we would have to
### write logic to pick the best match

regex_find = re.findall(r'href="(.*)">Historical Inflation Rates: ', our_site)

### uncomment to print the object and it's type
print(regex_find)
print(type(regex_find))

#grabs the first(and only) index of array regex_find
our_sub_site = urllib2.urlopen(regex_find[0]).read()