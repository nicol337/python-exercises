from dqueue import Queue


def hotPotato(players, num):
	q = Queue()
	for player in players:
		q.enqueue(player)
	while q.size() > 1:

		for turn in range(num):
			q.enqueue(q.dequeue())
		q.dequeue()

	winner = q.dequeue()
	return winner

def main():
	print(hotPotato(["Bill","David","Susan","Kent","Brad"],7))

main()