// returns binary gap of integer

function binary_gap(N){

	// convert to binary
	N = N.toString(2)

	// remove trailing/leading zeros
	N = N.replace(/^0+|0+$/g,"")

	// split by '1' digits
	N = N.split('1')

	// convert '0' strings to character counts
	for(i = 0; i < N.length; i++){
		N[i] = N[i].length
	}
	// return highest character count
	return(Math.max.apply(Math,N))
}

// testing:
console.log("console.log(9); expect 2: "+binary_gap(9))
console.log("console.log(529); expect 4: "+binary_gap(529))
console.log("console.log(20); expect 1: "+binary_gap(20))
console.log("console.log(15); expect 0: "+binary_gap(15))

