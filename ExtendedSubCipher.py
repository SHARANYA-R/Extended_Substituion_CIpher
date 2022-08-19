import random
import string


class ExtendedSubCipher:
	def __init__(self, key):
		self._charset = string.ascii_letters+string.digits+string.punctuation+" "
		seed, no_of_tables = key.split(".")
		random.seed(seed)
		self._tables = list()
		self.starting_table_index = 0
		for _ in range(int(no_of_tables)):
			temp = list(self._charset)
			random.shuffle(temp)
			self._tables.append(''.join(temp))
		
	def reset_starting_table_index(self):
		self.starting_table_index = 0

	
	def encrypt(self, text):
		final=""
		_length = len(self._tables)
		for letter in text:
			temp = self._tables[(self.starting_table_index)%_length][self._charset.index(letter)]
			final += temp
			self.starting_table_index = (self.starting_table_index +1)%_length
		print("+++++++++++++++After encryption++++++++++++++")
		# self.pprint()
		return final

	def decrypt(self, text):
		final=""
		_length = len(self._tables)
		for letter in text:
			temp = self._charset[self._tables[self.starting_table_index % _length].index(letter)]
			final += temp
			self.starting_table_index = (self.starting_table_index +1)%_length
		print("+++++++++++++++After Decryption++++++++++++++")
		# self.pprint()
		return final

	def pprint(self):
		print("all char: ",self.__all_char)
		print("__seed: ",self.__seed)
		print("__number_of_lists: ",self.__number_of_lists)
		print("__list_of_random_lists: ",self.__list_of_random_lists)