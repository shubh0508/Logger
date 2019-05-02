import psycopg2

class Database:

	def __init__(self, config):
		self.__config = config

		if self.__checkConfig() == False:
			raise Exception('Incorrect configuration provided ' + str(config))

		self.__connection = None
		self.__initializeConnetion

	def __checkConfig(self):

		if self.__config is None or \
		'host' not in self.__config or \
		'username' not in self.__config or \
		'database' not in self.__config or \
		'password' not in self.__config :
			return False

		return True

	def __initializeConnetion(self):

		host = self.__config['host']
		username = self.__config['username']
		database = self.__config['database']
		password = self.__config['password']

		port = 5432
		if port in self.__config:
			port = self.__config['port']

		self.__connection = psycopg2.connect(database = database,
			user = username,
			password = password,
			host = host,
			port =port)

		return

	def __getConnection(self):
		if self.__connection is None:
			self.__initializeConnetion()

		return self.__connection

	def closeConnection(self):
		if self.__connection is not None:
			self.__connection.close()

		return

	def executeQuery(self, query):

		rowsModified = 0
		try:
			connection = self.__getConnection()

			cursor = connection.cursor()
			cursor.execute(query)

			connection.commit()
			rowsModified = cursor.rowcount

		except (Exception, psycopg2.Error) as error:
			raise Exception('SQL QUERY Exception ' + str(error))

		# print('Result', query, rowsModified)
		return rowsModified