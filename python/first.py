print("Hello World!")
SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}
s = [1,2,3,4,5,6,7]

for x in s: 
	print(x)

d = [ 2*x for x in s]

print(d)


str = ["a","d","a","c","d","e","d","f"]
from collections import Counter
counts = Counter(str)
print(counts.most_common(3))