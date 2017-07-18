from sys import argv

script, a = argv
arr = []
num = int(a)
d = 0
for i in xrange(0,8):
	k = num >> i
	print k
	k ^= 1
	print k
	d |= k << i
	print d
	arr.append(k)

print d