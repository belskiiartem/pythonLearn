stringToParse="Python hAs an amazing fEature"
charToFind = ['a', 'e', 'i', 'o', 'u']
i = 0
for char in charToFind:
	print ('Count for ',char,' ', stringToParse.count(char))
	i = i + 1