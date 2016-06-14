#mengambil nama yang berada di posisi ke 'pos' dan di iterasi selama 'count' kali

import urllib
from BeautifulSoup import *

sample_data = 'http://python-data.dr-chuck.net/known_by_Fikret.html'
actual_data = 'http://python-data.dr-chuck.net/known_by_Ruaidhri.html'

url = raw_input("Enter URL: " )
count = raw_input("Enter count:" )
pos = raw_input("Enter position:" )


html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
print "Retrieving:" + url

i = 0
while (i < count):	
	tags = soup('a')
	list_url = []
	for tag in tags:
		list_url.append(str(tag.get('href', None)))
	print "Retrieving:" + list_url[pos-1]
	html = urllib.urlopen(list_url[pos-1]).read()
	soup = BeautifulSoup(html)	 	
	i = i + 1

