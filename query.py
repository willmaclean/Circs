# Given a db of P2P transactions with account to, account from, amount, information,
 # this extracts the network information and stores it as an dataframe in memory
 #use this if you can't be bothered to write your own SQL query

def query(db: dict, tablename = None, *args):

	"""
	Arguments:

	db: a dictionary with keys ['user','password','host', 'port', 'database']

	tablename: name of the table
	columns: the columns of the SQL database that you want 

	*args: should be strings of column names you want. If there are none, this function will select those which have a 'from', 'to', 'value/amount', and 'time'.


	"""

	import sys 
	import numpy as np
	import warnings
	warnings.filterwarnings('ignore')
	import pandas as pd 
	import time
	import os
	import psycopg2

	#creating a cursor
	def newCursor(db):
	    try:
	        connection = psycopg2.connect(user = os.environ[db['user']]
	                                      password = os.environ[db["password"]],
	                                      host = os.environ[db["host"]],
	                                      port = db["port"],
	                                      database = os.environ[db["database"]])

	        cursor = connection.cursor()
	        return cursor


	    except (Exception, psycopg2.Error) as error:
	        print("Error while connecting to PostgreSQL", error)
	        return error



	#formatting the columns into a string for the cursor query
	columns_to_get = ""

	if args:

		for arg in args:

			columns_to_get += ', ' + arg.lower
	else:

		columns_to_get = "*"


	#making the query
	query_string = f"""SELECT {columns_to_get}       
            FROM {tablename};"""

	c = newCursor()
	c.execute(query_string)
	transactions = pd.DataFrame(c.fetchall()).set_index('index')

	if args:

		transactions.columns = [arg for arg in args]

	return transactions
