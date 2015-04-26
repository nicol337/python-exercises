try:
	with open('file','r') as f:
		print(f.readline())
except(IOError, SyntaxError):
	print('error')
else:
	print('no error')