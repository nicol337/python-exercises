
class HashTable:
	def __init__(self):
		self.size = 11
		self.slots = [None]*self.size
		self.data = [None]*self.size

	def put(self, key, data):
		hash_val = self.getHash(key)
		if not self.slots[hash_val]:
			self.slots[hash_val] = key
			self.data[hash_val] = data
		elif self.slots[hash_val] == key:
			self.data[hash_val] = data
		else:
			placed = False
			while not placed:
				new_hash = self.getNewHash(hash_val)
				hash_val = new_hash
				if not self.slots[new_hash]:
					self.slots[new_hash] = key
					self.data[new_hash] = data
					placed = True

	def get(self,key):
		hash_val = self.getHash(key)
		if self.slots[hash_val] == key:
			return self.data[hash_val]
		else:
			num_checked = 0
			while num_checked < self.size:

				new_hash = getNewHash(hash_val)
				hash_val = new_hash
				if self.slots[new_hash] == key:
					return self.data[new_hash]
				num_checked += 1
		return None



	def getHash(self,key):
		return key%self.size

	def getNewHash(self,hash_val):
		return (hash_val+1)%self.size


	def __getitem__(self,key):
		return self.get(key)

	def __setitem__(self,key,data):
		self.put(key,data)