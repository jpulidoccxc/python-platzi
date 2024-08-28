import sys
#print(sys.path)

import re
text = 'Mi numero de telefono es 311 123 121, el codigo del pais es 57, mi numero de la suerte es 6'

result = re.findall('[0-9]+', text)
print(result)

import time
timestamp = time.time()
local = time.localtime()
resultTime = time.asctime(local)
print('unix', timestamp)
print(resultTime)

import collections
numbers = [1,1,2,2,3,35,46,584,8,152,13,2,1]
counter = collections.Counter(numbers)
print(counter)