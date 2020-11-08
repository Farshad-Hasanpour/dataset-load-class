import gzip
import json
import csv


class Dataset:
	def __init__(self, filename):
		self.filename = filename

	def read_json(self, useful_keys=(), required_keys=(), is_gzip=False, encoding='utf8'):
		"""
		:param useful_keys: (tuple): Keys to return for each dataset record. Pass empty to return all keys.
		:param required_keys: (tuple): Required keys for each record. If one of these keys does not exist, this function ignores the dataset record.
		:param is_gzip: (boolean): Whether the file is a compressed file or not.
		:param encoding: (string): The default is 'utf8'.
		:return: (list of dictionary): For each JSON record, return a dictionary inside a list.
		"""
		dataset = list()
		if is_gzip:
			open_function = gzip.GzipFile
		else:
			open_function = open
		# Load dataset file
		with open_function(self.filename, 'rb') as file:
			# For each record in dataset
			for line in file:
				data = json.loads(line, encoding=encoding)
				# By default get the dataset record
				append_record = True
				# If required keys does not exist do not get the record otherwise
				for key in required_keys:
					if not data.get(key):
						append_record = False
						break
				# get useful reviews
				if append_record:
					# Determine useful keys
					useful = ()
					if 0 == len(useful_keys):
						useful = data.keys()
					else:
						useful = useful_keys
					temp = {}
					for key in useful:
						temp[key] = data.get(key)
					dataset.append(temp)
		return dataset

	def read_csv(self, useful_keys=(), required_keys=(), delimiter=',', is_gzip=False, encoding='utf8'):
		"""
		:param useful_keys: (tuple or string): Keys to return for each dataset record. Pass empty to return all keys.
		:param required_keys: (tuple): Required keys for each record. If one of these keys does not exist, this function ignores the dataset record.
		:param delimiter: (string): CSV delimiter
		:param is_gzip: (boolean): Whether the file is a compressed file or not.
		:param encoding: (string): The default is 'utf8'.
		:return: (list of list | list): For each CSV row, return a list inside another list and a list of headers.
		"""
		dataset = list()
		if is_gzip:
			open_function = gzip.open
		else:
			open_function = open
		# Load dataset file
		with open_function(self.filename, mode='rt', encoding=encoding) as file:
			content = csv.reader((line.replace('\0', '') for line in file), delimiter=delimiter)
			# Get keys of dataset

			headers = next(content)
			# Transform keys to index
			useful = []
			required = []
			if 0 == len(useful_keys):
				iteration = headers
			else:
				iteration = useful_keys
			for key in iteration:
				useful.append(headers.index(key))
			for key in required_keys:
				required.append(headers.index(key))
			# For each record in dataset
			for row in content:
				if not row:
					continue
				# By default get the record from dataset
				append_record = True
				# If one of required keys does not exists ignore this dataset record otherwise get the record
				for i in required:
					if row[i] == '':
						append_record = False
						break
				if append_record:
					dataset.append(list(row[index] for index in useful))
			return dataset, headers

