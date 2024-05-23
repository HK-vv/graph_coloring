import random

def gen_edges(n, edges_num, seed):
	random.seed(seed)
	edges=[]
	while len(edges)<edges_num:
		u=random.randint(0,n-1)
		v=random.randint(0,n-1)
		if u != v and (u, v) not in edges and (v, u) not in edges:
			edges.append((u, v))
	return edges
