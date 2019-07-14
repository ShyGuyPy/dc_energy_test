import urllib2 as ul
import re
import numpy

our_site = ul.urlopen("https://www.usinflationcalculator.com/inflation/").read()



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
print(regex4)


our_sub_site = ul.urlopen(regex4[0]).read()
#print(our_sub_site)
#our_sub_site = urllib2.urlopen("https://www.usinflationcalculator.com/inflation/historical-inflation-rates/").read()
#print(our_sub_site)

#r"\"\[.+\]\""

regex_th1 = re.findall(r'<th scope="\col"\ valign="top">(.*)</th>', our_sub_site)
regex_th2 = re.findall(r'<th scope="row">(.*)</th>', our_sub_site)

regex_td = re.findall(r'<td align="center">(.*)</td>', our_sub_site)


#print(regex_th1)
#print(regex_th2)
print(regex_td)






#https://www.usinflationcalculator.com/inflation/historical-inflation-rates/

#                                                                                <a href="https://www.usinflationcalculator.com/inflation/historical-inflation-rates/" class="bump-view" data-bump-view="tp">
#                                                Historical Inflation Rates: 1914-2019                                   </a>


#https://www.guru99.com/python-regular-expressions-complete-tutorial.html#5