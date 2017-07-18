count = 1
print "%d, %s" % (count, True and True )
count += 1
print "%d, %s" % (count, False and True )
count += 1
print "%d, %s" % (count, 1 == 1 and 2 == 1 )
count += 1
print "%d, %s" % (count, "test" == "test" )
count += 1
print "%d, %s" % (count, 1 == 1 or 2 != 1 )
count += 1
print "%d, %s" % (count, True and 1 == 1 )
count += 1
print "%d, %s" % (count, False and 0 != 1 )
count += 1
print "%d, %s" % (count, True or 1 == 1 )
count += 1
print "%d, %s" % (count, "test" == "testing" )
count += 1
print "%d, %s" % (count, 1 != 0 and 2 == 1 )
count += 1
print "%d, %s" % (count, "test" != "testing" )
count += 1
print "%d, %s" % (count, "test" == 1 )
count += 1
print "%d, %s" % (count, not (True and False) )
count += 1
print "%d, %s" % (count, not (1 == 1 and 0 != 1) )
count += 1
print "%d, %s" % (count, not (10 == 1 or 1000 == 1000) )
count += 1
print "%d, %s" % (count, not (1 != 10 or 3 == 4) )
count += 1
print "%d, %s" % (count, not ("testing" == "testing" and "Zed" == "Coll Guy") )
count += 1
print "%d, %s" % (count, 1 == 1 and (not ("testing" == 1 or 1 == 0)) )
count += 1
print "%d, %s" % (count, "chunky" == "bacon" and (not (3 == 4 or 3 == 3)) )
count += 1
print "%d, %s" % (count, 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun")) )