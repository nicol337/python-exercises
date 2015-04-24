from dqueue import Queue
def main():
	q = Queue()
	print(q.isEmpty())
	q.enqueue('a')
	print(q.isEmpty())
	q.enqueue('b')
	q.enqueue('c')
	print(q.size())
	print(q.dequeue())
	print(q.size())
	print(q.dequeue())
	print(q.size())
	print(q.dequeue())
	print(q.size())
	print(q.isEmpty())
	q.enqueue('d')
	q.enqueue('a')
	print(q.dequeue())
	print(q.size())
	print(q.isEmpty())
	print(q.dequeue())


if __name__ == "__main__":
	main()