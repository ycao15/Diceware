import csv

'''
I dumped the contents of the diceware list with the command: 
	od -c diceware.txt
Each key in the file is followed by a "tab" character('\t')
Each word in the file is followed by a newline character('\n')
'''

#mapFile = open("diceware_cpp_map_init.txt", "a")
mapFile = open("temp.txt", "a")

mapFile.write('{\n')

with open('original_diceware_list.txt') as tsvfile:
	reader = csv.reader(tsvfile, dialect='excel-tab')
	for line in reader:
		mapFile.write('{' + line[0] + ',"' + line[1] + '"}, ')

mapFile.write("}")

mapFile.close()
