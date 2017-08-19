try:
	from quantumrandom import randint
	from sys import stdout
except ImportError:
	import pip
	print("*** Installing Quantum Random package")
	pip.main(['install', 'quantumrandom'])
	print('')

# generates the key
def dice():
	key = []
	for i in range(5):
		x = randint(1, 7)
		stdout.write(str(x))
		stdout.flush()
		key.append(str(x))
	print('')
	return int(''.join(key))

# load the dictionary of words to use from dictionary.txt
dictionary = {}
with open("dictionary.txt") as f:
	for line in f:
		(key, val) = line.split()
		dictionary[int(key)] = val
	f.close()

nWords = int(input("number of words [5,10]: "))
if nWords < 5:
	nWords = 5
elif nWords > 10:
	nWords = 10

print("Generating keys...")

passphrase = ""
for i in range(nWords):
	passphrase += dictionary[dice()] + " "

print(passphrase)
