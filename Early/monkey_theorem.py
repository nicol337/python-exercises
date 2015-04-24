import random


def random_word(letters, word_len):

	word = ""
	for i in range(word_len):
		word += random.choice(letters)
	return word


def word_scorer(match_str, random_str):
	

# def check_word_match():


def main():
	letters = [chr(i) for i in range(97,97+26)]
	letters.append(' ')
	match_str = "methinks it is like a weasel"
	print(letters)

	random_str = random_word(letters, len(match_str))
	print(random_str)
	counter=1
	while (random_str != match_str):
		random_str = random_word(letters, len(match_str))
		print(random_str)
		counter+=1

	

if __name__ == "__main__":
	main()
