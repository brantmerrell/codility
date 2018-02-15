def binary_gap(N):

	# convert to binary string
	B = str(bin(N))
	import re

	# remove "0b" from binary string
	B = re.sub("0b","", B)

	# remove leading & trailing zeros
	gp = re.sub("^0+|0+$","", B).split("1")

	# convert each zeros string to a character count
	for i in range(0, len(gp), 1): gp[i] = gp[i].count("")-1


	return(max(gp))


