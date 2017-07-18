from sys import argv
from sys import exit
import Tkinter
import time
from Tkconstants import *
from Tkinter import *
import  myGraph
import point2d

script, maze, name, fn, namef = argv
root = Tk()
canvas = Canvas(root, width = 1200, height = 700, bg = 'black')
name_of_algorithm = namef.upper()
root.title(name_of_algorithm)
canvas.pack()

MAZE = []
txt = open(name)
MAZE = txt.readlines()
txt.close()
n = len(MAZE)
m = len(MAZE[0])
w = 1200 / (m-1)
h = 700 / n
hi = we = 0


for i in xrange(0, n):
	for j in xrange(0, m-1):
		if MAZE[i][j] == "%":
			canvas.create_rectangle(we , hi, we + w,hi + h, fill = "blue")
		if MAZE[i][j] == "P":
			Pac = canvas.create_oval(we , hi, we + w,hi + h, fill = "LightSlateGray")
			Pos_Pac = point2d.Point2d(j, i)
		if MAZE[i][j] == "G":
			canvas.create_rectangle(we , hi, we + w,hi + h, fill = "red")
			Pos_Gold = point2d.Point2d(j, i)
		we += w
	hi += h
	we = 0

g = myGraph.MyGraph(MAZE)
d = g.Successor(Pos_Pac)
p =  [[point2d.Point2d(0,0) for i in xrange(1,len(MAZE[0]))] for j in xrange(1,len(MAZE))]


has_a_pass = False

if name_of_algorithm == "DFS":
	has_a_pass = g.runDFS(Pos_Pac,Pos_Gold, p)
elif name_of_algorithm == "BFS":
	has_a_pass = g.runBFS(Pos_Pac,Pos_Gold, p)
elif name_of_algorithm == "UCS":
	has_a_pass = g.runUCS(Pos_Pac,Pos_Gold, p)

txt = open("Solution.txt","w")
if has_a_pass:
	path = g.conver_to_Path(p, Pos_Pac, Pos_Gold)
	
	txt.write("%d\n" % len(path))
	for i in xrange(0, len(path) - 1):
		d = path[i].Decisions( path[i + 1])
		txt.write(d + " "),
		if d == "U" or d == "D":
			if d == "U":
				canvas.move(Pac, 0, - h)
			else:
				canvas.move(Pac, 0,  h)
		elif d == "L" or d == "R":
			if d == "L":
				canvas.move(Pac, -w, 0)
			if d == "R":
				canvas.move(Pac, w, 0)
		root.update()
		time.sleep(0.15)
	txt.close()
	exit(0)
	# canvas.mainloop()
else:
	print "Don't have a path"
	txt.write("Null")
	txt.close()
exit(1)