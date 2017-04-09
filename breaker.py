# open input file 

# count A's, B's, C's, etc. 

# report counts. 

# guess a key, and show the user the key, and the translation

# allow user to make changes 

# hmm
import sys

ciphertext_file = sys.argv[1]
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
freq = ["E", "T", "A", "O", "I", "N", "S", "H", "R", "D", "L", "C", "U", "M", "W", "F", "G", "Y", "P", "B", "V", "K", "J", "X", "Q", "Z"]

ctext = []
with open(ciphertext_file) as f: 
	while True: 
		c = f.read(1)
		ctext.append(c)		
		if c == "": 
			break
		i = 0 
		for ele in alphabet:						
			if c == ele: 
				counts[i] = counts[i] + 1 
			i = i + 1
f.close()

with open(ciphertext_file) as f: 			
	#make long string
	cipherstr = f.read()
f.close()

#display cipher txt
print "Ciphertext\n%s" % cipherstr
print "length: %d\n" % len(cipherstr)
			
# make tuple 
tcounts = []
for x in range(0, 26): 
	tcounts.append((alphabet[x], counts[x]))
			
# report counts 
print "Letter Frequencies"
	
#sort tuple 
def getKey(item): 
	return item[1]
sorted_tcounts = sorted(tcounts, key=getKey, reverse=True)
for ala in sorted_tcounts: 
	print "%2s" % ala[0],
print ""
for ala in sorted_tcounts: 
	print "%2d" % ala[1],
print "\n"

tkey = []
i = 0
for t in sorted_tcounts:	
	tkey.append( (t[0], freq[i]) )
	i = i + 1
	
print "Possible Key"
print "ct: ",	
for r in tkey:
	print "%1s" % r[0],
print "\npt: ",	
for r in tkey:
	print "%1s" % r[1],
print "\n"
	
# decrypt and display
while True:
	ptext = [] 
	for l in ctext:
		for q in tkey: 
			if l == q[0]: 
				ptext.append(q[1])
				
	ptextstr = "".join(ptext)				 
	print ptextstr
	print "length: %d" % len(ptextstr)
		
	requested_change = raw_input('\nEnter a key change you would like to make.\ne.g., enter fe to make ciphertext F become plaintext E.\nk, go: ')	
	ct = requested_change[0]
	pt = requested_change[1]

	i = 0
	for t in tkey:
		if ct == t[0]:
			tkey[i] = (ct, pt)
		i = i + 1
	
	print "\nNew Key"
	print "ct: ",	
	for r in tkey:
		print "%1s" % r[0],
	print "\npt: ",	
	for r in tkey:
		print "%1s" % r[1],
	print "\n"

	#display cipher txt
	print "Ciphertext\n%s\n" % cipherstr
	print len(cipherstr) 
	
	print "Letter Frequencies"
	for ala in sorted_tcounts: 
		print "%2s" % ala[0],
	print ""
	for ala in sorted_tcounts: 
		print "%2d" % ala[1],
	print "\n"	
