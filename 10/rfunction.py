"""DEBUG"""
# reverse a string, Hussein Suleman, 18 March 2015.

def reverse_string (sentence):
	"""DEBUG""";print('reverse_string')
	new_sent = ""
	for i in range (len (sentence)-1,-1,-1):
		new_sent = new_sent + sentence[i]
	return new_sent

def main ():
	"""DEBUG""";print('main')
	sent = input ("Enter a sentence: ")
	print (reverse_string (sent))
	print (reverse_string (sent+sent))

main()