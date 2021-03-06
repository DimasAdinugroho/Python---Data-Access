#Program ini membaca XML dari URL yang di input oleh user, kemudian mengextract Tag <count> dan mengambil valuenya kemudian dihitung jumlah valuenya

import urllib
import xml.etree.ElementTree as ET

sample_data = 'http://python-data.dr-chuck.net/comments_42.xml'
actual_data = 'http://python-data.dr-chuck.net/comments_270773.xml'

data = urllib.urlopen(sample_data).read()
root = ET.fromstring(data) #root merupakan commentinfo
print root.tag #return commentinfo

#CARA PERTAMA, menggunakan findall
results = root.findall('comments/comment')
x = 0
for item in results:
	x = x + int(item.find('count').text)	
print x

#CARA KEDUA, memparsing root secara langsung
i = 0
for child in root[1]: #ambil semua isi comments
	i = i + int(child.find('count').text) #ambil semua value pada tag <count>, ubah ke integer dan jumlahkan
print i

'''
<commentinfo> #root
	<note>This file contains the sample data for testing</note> #posisi root[0]
	<comments>					#posisi root[1]
		<comment> 				#posisi root[1][0]
			<name>Romina</name> #posisi root[1][0][0]
			<count>97</count>	#posisi root[1][0][1]
		</comment>
		<comment>				#posisi root[1][1]
			<name>Laurie</name> #posisi root[1][1][0]
			<count>97</count>	#posisi root[1][1][1]
		</comment>
	</comments>
</commentinfo>
'''
