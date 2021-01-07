
class Pairs:

	def self.__init__(self):
		
		self.pair_ids_ = None


	def fit(self, transactions):

		#this searches for 'from','to',and 'amount' columns

		flipped = transactions.copy().rename(columns={'from':'to','to':'from','amount':'amount'})
		back_and_forth = pd.concat([to_and_fro, flipped])[['to','from']]
		self.pair_ids_ = back_and_forth[back_and_forth.duplicated()].to.values


	def get_pair_transactions(self, transactions):

		return transactions.iloc[self.pair_ids_]


	def get_pair_graph(self, draw=False):

		import networkx
		G = networkx.Graph()
		G.add_edges_from(transactions.iloc[self.pair_ids_][['to','from']].values)
		if draw:
			networkx.draw(G, with_labels=True)
		return G


class Cliques:

	def self.__init__(self)



	