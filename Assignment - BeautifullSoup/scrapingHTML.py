import urllib
from BeautifulSoup import *

sample_data = 'http://python-data.dr-chuck.net/comments_42.html'
actual_data = 'http://python-data.dr-chuck.net/comments_270776.html'

html = urllib.urlopen(actual_data).read()
soup = BeautifulSoup(html)

tags = soup('span') #ambil semua tag <a></a>

print sum([int(i) for i in re.findall('[0-9]+',str(tags).strip('[]'))])

