import re
#print sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] )
#print open('regex_sum_test.txt', 'r').read()
#print sum([1,2,3,4,5])
print sum([int(i) for i in re.findall('[0-9]+',open('regex_sum.txt', 'r').read())])

