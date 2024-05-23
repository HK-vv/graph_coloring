from problem_convert import graph_coloring2cnf, dec
from data_gen import gen_edges
from graph_drawing import draw_graph
from pysat.formula import CNF
from pysat.solvers import Solver

SEED=666
n=10
m=20
E=gen_edges(n=n, edges_num=m, seed=SEED)
G=(n,E)
print("data prepared.")
draw_graph(G, target='original.png')
PRINT_GRAPH=False
if PRINT_GRAPH:
	for (u,v) in E:
		print(u,v)


if __name__=='__main__':
	
	for c in range(1,n+1):
		clauses=graph_coloring2cnf(G, c)
		# Now call the SAT solver.
		cnf = CNF(from_clauses=clauses)
		with Solver(bootstrap_with=cnf) as solver:
			solved=solver.solve()
			print(f"graph G IS{' NOT' if not solved else ''} {c}-colorable")
			if solved:
				print(f"\\chi(G)={c}")
				model=solver.get_model()
				color=[]
				for z in model:
					if z>0:
						color.append(dec(z,c))
				print(f"a legal coloring scheme is\n{color}")
				draw_graph(G, color=color, target='with_color.png')
				break
