from random import SystemRandom

# generate random number between 1 and 6 inclusive
def random():
	return SystemRandom().randrange(1,7) # uses /dev/urandom which is fairly secure

# generates the key
def dice():
	key = random()
	key += random() * 10
	key += random() * 100
	key += random() * 1000
	key += random() * 10000
	return key

# load the dictionary of words to use from dictionary.txt
dictionary = {}
with open("dictionary.txt") as f:
	for line in f:
		(key, val) = line.split()
		dictionary[int(key)] = val
	f.close()

# for python 3, change raw_input to input
numberOfWords = int(raw_input("number of words in passphrase (at least 5): "))
if (numberOfWords < 5):
	numberOfWords = 5

passphrase = ""
for i in range(numberOfWords):
	passphrase += dictionary[dice()] + " "

print passphrase