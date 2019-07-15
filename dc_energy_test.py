### run 'pip install requirements(witht the requirements.txt file in the same directory)
### should install the same versions of the packages I used in my venv

### all test were run with python version 2.7

### imports urllib2 to grab site source code and re to handle regular expressions in python(to parse source code)
import urllib2
import re
import numpy as np
import pandas as pd

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
# print(regex_find)
# print(type(regex_find))

#grabs the first(and only) index of array regex_find
our_sub_site = urllib2.urlopen(regex_find[0]).read()

regex_month = re.findall(r'<th scope="\col"\ valign="top">(.*)</th>', our_sub_site)
regex_year = re.findall(r'<th scope="row">(.*)</th>', our_sub_site)

regex_td = re.findall(r'<td align="center">(.*)</td>', our_sub_site)

###here I create containers and a count variable
this_row = []
bucket = np.empty((0,13), int)
count = 0

#### now I iterate through the data, splitting it into arrays of 13 indexes to fit
### the dataframe that I'll construct soon
for i in regex_td:
    count +=1
    this_row.append(i)
    if count%13 ==0:
        bucket = np.append(bucket, np.array([this_row]), axis=0)
        this_row = []

### and here I throw all the pieces into a pandas dataframe
my_dataframe = pd.DataFrame.from_records(bucket, index = regex_year, columns = regex_month)
### I sort the dataframe before I make any other changes to it
my_dataframe.sort_values(by=['Ave'], inplace=True, ascending=False)

display = my_dataframe['Ave']
display = display.drop(['2019'])

###for parsing the rest of the html I'll import BeautifulSoup, since I've hit the limits
###of my regex knowledge
from bs4 import BeautifulSoup
soup_test = BeautifulSoup(our_sub_site, 'html.parser')
soup_para = soup_test.p
soup_print = soup_para.get_text()

###finally I print all the pieces
print(soup_print.encode("utf-8"))
print("Year      Average")
print(display)