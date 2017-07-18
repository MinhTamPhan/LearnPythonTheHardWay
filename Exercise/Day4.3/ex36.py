from string import *
from random import randint
from sys import exit

Option = ['KEO','BUA','BAO']
while True:
	print Option, "q is quit."
	user = raw_input("> ")
	user = upper(user)
	if user == 'Q':
		exit(0)
	com = randint(0,2)
	print "Com: %s - user: %s" % (Option[com], user)
	if Option[0] in user:
		if Option[com] == 'KEO':
			print "\tHoa."
		elif Option[com] == 'BUA':
			print "May thang. You Lose."
		else:
			print "Ban thang. You Win."


	elif Option[1] in user:
		if Option[com] == 'KEO':
			print "Ban thang. You Win."
		elif Option[com] == 'BUA':
			print "\tHoa."
		else:
			print "May thang. You Lose."

	elif Option[2] in user:
		if Option[com] == 'KEO':
			print "May thang. You Lose."		
		elif Option[com] == 'BUA':
			print "Ban thang. You Win."
		else:
			print "\tHoa."
	else:
		print "You need to learn 'Oan-Tu-Ti'"