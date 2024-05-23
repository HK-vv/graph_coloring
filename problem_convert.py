def dec(z, c):
	z-=1
	return (z//c, z%c)

def graph_coloring2cnf(G, c):
	"""
	G is a graph that contains vertex {0,1,2,...,n-1}, and edges E={(u,v)}
	c is the coloring number 
	"""
	n,E=G
	clauses=[]
	def inc(x,y):
		return x*c+y+1
	# first condition
	for i in range(n):
		tl=[]
		for j in range(c):
			tl.append(inc(i,j))
		clauses.append(tl)
	# second
	for i in range(n):
		for k in range(c):
			for j in range(k+1,c):
				clauses.append([-inc(i,k),-inc(i,j)])
	# third
	for (u,v) in E:
		for k in range(c):
			clauses.append([-inc(u,k),-inc(v,k)])

	return clauses
	