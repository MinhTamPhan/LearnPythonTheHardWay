from sys import argv

script, Num = argv

n = int(Num)

arr = []
arr2 = []

num = 0
while n != 0:
	arr.append(n % 10)
	arr2.append(arr[num])
	n /= 10
	num += 1

for i in xrange(0,arr.__len__() - 1):
	for j in xrange(i + 1,arr.__len__() - 1):
		if arr2[i] > arr2[j]:
			temp = arr2[i]
			arr2[i] = arr2[j]
			arr2[j] = temp
print arr2
ischange = False
for i in range(arr.__len__() - 2, 0 , -1):
	for j in range(i - 1, 0, -1):
		if(arr[i] > arr2[j]):
			temp = arr2[j]
			arr2[j] = arr2[i]
			arr2[i] = temp
			ischange = True
			break

if(ischange == False):
	for j in range(arr2.__len__() - 2, 0, -1):
		if(arr[i] > arr2[j]):
			temp = arr2[j]
			arr2[j] = arr2[i]
			arr2[i] = temp
			ischange = True
			break
if(ischange == False):
	print 0
else:
	rsl = 0
	for i in xrange(arr2.__len__() - 1, 0, -1):
		rsl = rsl * 10 + arr2[i]

	print rsl
