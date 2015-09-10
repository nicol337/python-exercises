
def findMovies(flight_length, movie_lengths):
	found_lengths = {}
	for t in movie_lengths:
		if (flight_length - t) in found_lengths:
			return True
		else:
			found_lengths[t] = True
	return False

print(findMovies(100,[50,40,60,70]))