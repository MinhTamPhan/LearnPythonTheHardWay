from sys import argv

script, inta, intb = argv
E = int(argv.__getitem__(1))
F = int(argv.__getitem__(2))
def gcd(a, b):
	if b == 0 :
		return a
	else :
		return gcd(b, a % b)

c =  gcd(E, F)
print c