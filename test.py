import urllib2 as ul
import re
import numpy as np
import pandas as pd

our_site = ul.urlopen("https://www.usinflationcalculator.com/inflation/").read()

#r'class="entry-content">

#regex1 = re.findall("<style>", our_site)
regex1 = re.findall(r"<script type='text/javascript'(.*)</script>", our_site)
regex2 = re.findall(r"src=\'(.*)\'", our_site)
regex3 = re.findall(r"<a href(.*)1914-2019", our_site)

#this one
regex4 = re.findall(r'href="(.*)">Historical Inflation Rates: ', our_site)
#test = regex1.group(0)
#print(regex1)

#print(regex2)
#print(regex1)
#print(regex4)


our_sub_site = ul.urlopen(regex4[0]).read()
#print(our_sub_site)
#our_sub_site = urllib2.urlopen("https://www.usinflationcalculator.com/inflation/historical-inflation-rates/").read()
#print(our_sub_site)

#r"\"\[.+\]\""

regex_para = re.findall(r'<p>(.*)</p>', our_sub_site)

#using negative lookback to get inverse of regex


regex_th1 = re.findall(r'<th scope="\col"\ valign="top">(.*)</th>', our_sub_site)
regex_th2 = re.findall(r'<th scope="row">(.*)</th>', our_sub_site)

regex_td = re.findall(r'<td align="center">(.*)</td>', our_sub_site)


#print(regex_th1)
#print(regex_th2)
#print(regex_td)

this_row = []
bucket = np.empty((0,13), int)
#bucket = []
count = 0

for i in regex_td:
    count +=1
    this_row.append(i)
    #print(this_row)
    if count%13 ==0:
        bucket = np.append(bucket, np.array([this_row]), axis=0)
        this_row = []

# headers = ()
# for i in regex_th1:
#     headers = headers + i
#
# print(headers)

headers = (regex_th1[0],regex_th1[1],regex_th1[2],regex_th1[3],regex_th1[4],regex_th1[5],regex_th1[6],
       regex_th1[7],regex_th1[8],regex_th1[9],regex_th1[10],regex_th1[11], regex_th1[12])
#
# my_data = (regex_th2, bucket)
# data_dict = dict(zip(headers, my_data))
# my_dataframe = pd.DataFrame(data_dict)
# print(my_dataframe)

test = pd.DataFrame.from_records(bucket, index = regex_th2, columns = headers)

#print(test)

#print("{}".format(len(regex_para2)))
# print(regex_para[0])#, regex_para[1])

#test_string = "sauce <a apple a>sauce   "

#regex_para2 = re.findall(r'(\s\<\s|\S\<|\<\s|\<|\s<.(.*)\s\>\s|\S\>|\>\s|\>)', test_string)
#regex_para2 = re.findall(r'(?! \<(.*)\> )', regex_para[0])
#test_reg = re.sub(r' <a ?:\/\/.*[\r\n]*', '', regex_para[0], flags=re.MULTILINE)
#print(test_reg)
#print(regex_para2)


from bs4 import BeautifulSoup
soup_test = BeautifulSoup(our_sub_site, 'html.parser')
soup_para = soup_test.p

soup_print = soup_para.get_text()
print(soup_print.encode("utf-8"))

#print("Year      Average")
test.sort_values(by=['Ave'], inplace=True, ascending=False)
display = test['Ave']
display = display.drop(['2019'])
#display.sort_values(by=['Ave'])
#display.sort_values(by=['Ave'], inplace=True, ascending=False)
#print(display)