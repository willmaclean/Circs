import unittest
import pandas as pd
from network import Pairs, find_subgraphs

class TestPairs(unittest.TestCase):

	def setUp(self):
		#load test data
		self.df_ = pd.read_pickle('fixtures/transactions_core_monthly_grouped.pkl')

	def test_input(self):
		with self.assertRaises(KeyError):
			self.df_[['to', 'from', 'amount']]

	def test_pairs(self):
		Pairs.fit(self.df_)
		pairs = pairs.get_pair_transactions(self.df_)
		pair_ids = Pairs.pair_ids_
		self.assertEqual(len(pair_ids), pairs.shape[1])

class Testsubgraph(unittest.TestCase):

	def setUp(self):
		self.df_ = pd.read_pickle('fixtures/transactions_core_monthly_grouped.pkl')

	def test_graph(self):
		G = find_subgraphs(self.df_)
		self.assertFalse(networkx.is_directed(G))

		

