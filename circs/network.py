from check import param_sanity

"""
Functions and classes which manipulate networks with a view to finding and analysing friendship circles. 

"""


class Pairs:

	"""
	The Pairs class finds pairs of nodes in the transaction ecosystem which transact back and forth with each other

	"""

	def __init__(self):
		
		self.pair_ids_ = None


	def fit(self, transactions):

		"""
		finds the pairs
		"""

		
		if param_sanity(transactions):

			#creating a df in which all transactions are also reversed
			flipped = transactions.copy().rename(columns={'from':'to','to':'from','amount':'amount'})
			back_and_forth = pd.concat([to_and_fro, flipped])[['to','from']]

			#saving the ids of the back and forth transacters
			self.pair_ids_ = back_and_forth[back_and_forth.duplicated()].to.values


	def get_pair_transactions(self, transactions):

		return transactions.iloc[self.pair_ids_]


	def get_pair_graph(self, draw=False):

		#creates an undirected graph of all the pair nodes

		import networkx
		G = networkx.Graph()
		G.add_edges_from(transactions.iloc[self.pair_ids_][['to','from']].values)
		if draw:
			networkx.draw(G, with_labels=True)
		return G


class Cliques:

	"""
	Cliques class finds and stores cliques, which are k-cores of the graph.
	"""

	def __init__(self):

		import networkx

		self.clique_ids_ = None
		self.clique_ = None

	def fit(self, transactions, k=3):

		"""
		creates the graph of cliques

		Arguments:
		--transactions: a pandas DF in usual format
		--k: the k of the core
		"""

		if param_sanity(transactions):

			trans_grouped = pd.DataFrame(transactions.groupby([['from','to']]).amount().sum()).reset_index()
			edges = np.array(trans_grouped).tolist()
			edges = [(edge[0], edge[1], float(edge[2])) for edge in edges]
			#making the graph
			dg = networkx.DiGraph()
			dg.add_weighted_edges_from(edges)
			self.clique_ = networkx.k_core(dg, k=k)
			self.clique_ids_ = list(self.clique_.nodes)

	def get_cliques_graph(self):

		"""
		returns the cliques graph

		"""

		return self.dg_


class Circs(Cliques):

	"""
	A circ is a pruned k-core. They are worked out as follows:

	1. All k-cores of a network are found.
	2. All nodes of degree < c are removed.
	3. All k'-cores of the resulting network are found.
	"""

	def __init__(self):

		import networkx

		Cliques.__init__(self)
		self.circ_ids_ = None
		self.circ_ = None
		self.df_ = None

	def fit(self, transactions, k=3, c = 2, k_prime= 2):

		"""
		creates the graph of circs

		Arguments:
		--transactions: a pandas DF in usual format
		--k: the k of the cores
		--c: the pruning threshold
		--kprime: the k of the new cores
		"""
		super().fit(self, transactions, k=3)
		d_under_c = []
		dg_pruned = self.clique_
		for node in dg_pruned.nodes:
		    if (dg_pruned.out_degree(node) < c ) & (dg_pruned.in_degree(node) < c ):
		        d_under_c.append(node)
		dg_pruned.remove_nodes_from(d_under_c)

		self.circ_ = networkx.k_core(dg_pruned, k=2)
		self.circ_ids_ = self.circ_.nodes
		self.df_ = transactions


	def get_circ_graph(self):

		"""
		returns the cliques graph

		"""

		return self.circ_

	def describe(self):

		return self.df_.describe()


def get_snapshot(G, date):

	"""
	Returns a snapshot of a multi-graph

	Arguments:

	G: a multigraph
	date: when the snapshot should be for

	Returns:

	An undirected graph
	"""
   

    # Find edges that existed during timestamp
    snapshot_edges = [(i,j,k) for i,j,k in G.edges if k==date]


    # Create network from edges
    return networkx.Graph(G.edge_subgraph(snapshot_edges))

def find_subgraphs(G, nodes):

	"""
	A generic function for producing a subgraph of G from a list of nodes. It reproduces the class of the original graph.
	"""

	SG = G.__class__()
	SG.add_nodes_from((n, G.nodes[n]) for n in nodes)
	if SG.is_multigraph():
	    SG.add_edges_from((n, nbr, key, d)
	        for n, nbrs in G.adj.items() if n in nodes
	        for nbr, keydict in nbrs.items() if nbr in nodes
	        for key, d in keydict.items())
	else:
	    SG.add_edges_from((n, nbr, d)
	        for n, nbrs in G.adj.items() if n in nodes
	        for nbr, d in nbrs.items() if nbr in nodes)
	SG.graph.update(G.graph)

	return SG






	