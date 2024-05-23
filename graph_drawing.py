import igraph
import random
import time

def draw_graph(G, target, color=None):
	n, E=G
	g=igraph.Graph(n=n, edges=E)
	if color is not None:
		random.seed(int(time.time()))
		c=max([y for x,y in color])+1
		cmap=[]
		for i in range(c):
			cmap.append((random.random(),
				random.random(),
				random.random()))
		pattern=[0]*n
		for x,y in color:
			pattern[x]=cmap[y]
	igraph.plot(g,
			 vertex_size=30,
			 vertex_label=list(range(n)),
			 vertex_color='white' if color is None else pattern,
			 target=target)
	