def a(str1, num):
	if num == 10 :
		return
	else :
		print str1, num
		a(str1,num + 1)

a("hello count ",0)