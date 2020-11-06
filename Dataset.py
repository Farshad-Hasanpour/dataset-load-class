import gzip
import json


class Dataset:
	def __init__(self, filename):
		self.filename = filename

	def read_json(self, required_keys, useful_keys, is_zip=False):
		"""
		:param required_keys: (set or list): keys that are required for each record
		:param useful_keys: (set or list): keys to pick from json file
		:param is_zip: (boolean): determines if the file is compressed
		:return: (list of dictionary): for each json record return a dictionary inside list
		"""
		dataset = list()
		if is_zip:
			open_function = gzip.GzipFile
		else:
			open_function = open
		# Load dataset file
		with open_function(self.filename, 'rb') as file:
			# for each review in dataset
			for line in file:
				# load one review from json file
				data = json.loads(line)
				# by default get the review
				get_review = True
				# If required keys does not exist do not get review
				for key in required_keys:
					if not data.get(key):
						get_review = False
						break
				# get useful reviews
				if get_review:
					dataset.append({key: data.get(key) for key in useful_keys})
		return dataset

