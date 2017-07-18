def gcd(a, b):
	if b == 0:
		return a
	else:
		return gcd(b, a % b)

def SumFaction(a, b, c, d):
	Tu = a * d + c * b
	Mau = b * d
	UCLN = gcd(Tu,Mau)
	return Tu / UCLN, Mau / UCLN

#rint SumFaction(3,6,2,8)

def SumListFaction(ListTubeF):
	sumf = (0,1)
	for item in ListTubeF:
		sumf= SumFaction(sumf[0], sumf[1], item[0], item[1]);
	return sumf

#a = [(1,2),(4,6),(1,5),(6,7),(1,9)]

#print SumListFaction(a)

def SumNumK(K):
	arr = []
	while K != 0:
		arr.append(K % 10)
		K /= 10
	return sum(arr)

K = 182034559

#print SumNumK(K)

def SumMatrix(a, b):
	result = []
	try:
		lena = len(a)
		lenb = len(b)
		if(lena != lenb):
			raise Exception("Size(a) != Size(b)")
		else:			
			for i in xrange(lena):
				rowa = []
				lenai = len(a[i])
				lenbi = len(b[i])
				if(lena != lenb):
					raise Exception("Size(a[i]) != Size(b[i])")
				else:					
					for j in xrange(lenai):
						rowa.append(int(a[i][j]) + int(b[i][j]))
					result.append(rowa)				
	except Exception as e:
		raise e
	return result

ma = ["123","456","789"]
mb = ["234","567","948"]

print SumMatrix(ma,mb)

def ThongKe(M):
	result = {}
	for row in M:
		for col in row:
			if col in result:
				result[col] += 1
			else:
				result[col] = 1
	return result

M = ["AKFB", "BDDC", "DFAK"]

#print ThongKe(M)