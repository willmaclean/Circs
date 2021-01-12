from network import get_snapshot

def draw_snapshot(G, num_dates)

"""
	To draw a snapshot of a multi-graph at a series of dates

	Arguments:
	G: the Multi-graph
	num_dates: the number of iterations into the graph that you want to show. 
"""



    for row in per_month.values:

        G.add_edge(row[1], row[2], key=row[0], weight = row[3])
    #drawing the sequence of the network across the first four weeks

    dates = [i for i in range(num_dates)]

    # Create a figure
    plt.figure(figsize=(10, 15))
    # Visualize the network for each date
    pos = None
    for i, date in enumerate(reversed(dates)):
        # Get a snapshot of the network
        G_ = get_snapshot(G, date)
        # Create a subplot
        plt.subplot(3, 2, num_dates - i)
        plt.title(date)
        # Calculate the layout
        #pos = networkx.spring_layout(G, pos=pos, k=0.09)
        # Visualize
        node_sizes = [G_.degree(node) * 220 for node in G_.nodes]
    #     all_edges = per_month[['from', 'amount']].set_index('from')
    #     colors = [np.log(float(all_edges[node])) for node in G_.nodes]
        networkx.draw_networkx(
            G_, #pos=pos, 
            alpha=0.5, edge_color='#333333', node_size=0.5,with_labels=False)

def plot_measure_as_series(G, measure, moments=[]):


	"""
		This function plots a time-series of a given global network measure through time.

		Arguments:
		G: the multi-graph
		measure: the global network measure to plot. Most common would be to use a networkx algorithm, but custom can be used. 
		moments: list. default None. If None, the function plots all moments in the graph. If specified, it only plots those given.
	"""	#you could ask people to make new connections

	# Create a figure
	plt.figure(figsize=(10, 15))
	# Visualize the network for each date

	pos = None
	y = []
	for i, moment in enumerate(reversed(moments)):
	    # Get a snapshot of the network
	    G_ = get_snapshot(SG, moment)
	    y.append(measure(G))
	plt.figure(figsize=(18,7))
	plt.plot(y)

