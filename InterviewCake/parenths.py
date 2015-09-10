
def parenthesis(sent, openParenthesis):
	paren = 1
	place = openParenthesis

	for c in sent[openParenthesis+1:]:
		if c == ')':
			paren -= 1
		elif c == '(':
			paren += 1
		if paren == 0:
			return place
		place += 1
	return -1






sentence = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
print(parenthesis(sentence,10))
