
def param_sanity(transactions):

	#performs a type check on the input df

	if set(transactions.columns) != {'from','to','amount'}:

			raise KeyError('most Circs classes require df columns to be labelled appropriately: [from, to, amount]')

	else:

		return True


