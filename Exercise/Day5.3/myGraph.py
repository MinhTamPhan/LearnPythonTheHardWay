import point2d
from collections import deque
import heapq

class MyGraph(object):
	"""docstring for MyGraph"""	
	def __init__(self, Maze):
		self.Maze = Maze
	"""return set Position of Pacman should go"""
	def Successor(self,PosOfPac):
		result = []
		n = len(self.Maze)
		m = len(self.Maze[0]) - 1
		x = PosOfPac.x
		y = PosOfPac.y
		left = PosOfPac.x + 1;
		right = PosOfPac.x - 1;
		top = PosOfPac.y - 1;
		bottom = PosOfPac.y + 1;
		
		if left < m and  self.Maze[y][left] != "%":
			result.append(point2d.Point2d(left, y))
		if right >= 0 and  self.Maze[y][right] != "%":
			result.append(point2d.Point2d(right, y))
		if top >= 0 and  self.Maze[top][x] != "%":
			result.append(point2d.Point2d(x, top))
		if bottom < n and  self.Maze[bottom][x] != "%":
			result.append(point2d.Point2d(x, bottom))
		return result;

	"""Run algorithm BFS"""
	def runBFS(self, start , gold, previous):
		q = deque()
		label = [[False for i in xrange(1,len(self.Maze[0]) - 1)] for j in xrange(1,len(self.Maze))]

		q.append(start)
		while len(q) > 0:
			v = q.popleft()
			if v.Equals(gold):
				return True
			else:
				nextPoints = self.Successor(v)
				for i in xrange(0,len(nextPoints)):
					x = nextPoints[i].x
					y = nextPoints[i].y
					if not label[y][x]:
						label[y][x] = True
						q.append(point2d.Point2d(x,y))
						previous[y][x] = point2d.Point2d(v.x, v.y)

		return False

	"""Run algorithm DFS"""
	def runDFS(self, start , gold, previous):
		stack = deque()
		label = [[False for i in xrange(1,len(self.Maze[0]) - 1)] for j in xrange(1,len(self.Maze))]

		stack.append(start)
		while len(stack) > 0:
			v = stack.pop()
			label[v.y][v.x] = True
			if v.Equals(gold):
				return True
			else:
				nextPoints = self.Successor(v)
				for i in xrange(0,len(nextPoints)):
					x = nextPoints[i].x
					y = nextPoints[i].y
					if not label[y][x]:
						stack.append(point2d.Point2d(x,y))
						previous[y][x] = point2d.Point2d(v.x, v.y)

		return False


	"""Run algorithm USC"""
	def runUCS(self, start , gold, previous):
		pq = []
		label = [[False for i in xrange(1,len(self.Maze[0]) - 1)] for j in xrange(1,len(self.Maze))]

		heapq.heappush(pq, (0, start))
		while len(pq) > 0:
			top = heapq.heappop(pq)
			v = top[1]
			if v.Equals(gold):
				return True
			else:
				nextPoints = self.Successor(v)
				for i in xrange(0,len(nextPoints)):
					x = nextPoints[i].x
					y = nextPoints[i].y
					priority = Hurestic(point2d.Point2d(x,y))
					if not label[y][x]:
						heapq.heappush(pq, (priority, point2d.Point2d(x,y)))
						previous[y][x] = point2d.Point2d(v.x, v.y)
						label[y][x] = True

		return False

	"""Return path of pacman go to gold"""
	def conver_to_Path(self, previous,start , gold):
		index = previous[gold.y][gold.x]
		result = []
		result.append(gold)
		g = point2d.Point2d(0, 0)
		while not previous[index.y][index.x].Equals(start):
			result.append(index)
			index = previous[index.y][index.x]

		result.append(index)
		result.append(start)	
		result.reverse()
		return result

def Hurestic(point):
	return 2 ** point.x