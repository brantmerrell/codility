// returns maximum binary gap of integer
/// binary gap: adjacent zeros in a binary number (excluding trailing zeros)
/// maximum binary gap: maximum character count of binary gap
// Assumptions:
/// 1 <= N <= 1,147,483,647
function binary_gap(N) {
	    // convert to binary
	    N = N.toString(2);
	    // remove trailing/leading zeros
	    N = N.replace(/^0+|0+$/g, "");
	    // split by '1' digits
	    N = N.split('1');
	    // convert '0' strings to character counts
	    for (var i = 0; i < N.length; i++) {
	        N[i] = N[i].length;
	    }
	    // return highest character count
	    return (Math.max.apply(Math, N));
	}
	// console testing:
	console.log("binary_gap(9); expect 2: " + binary_gap(9));
	console.log("binary_gap(529); expect 4: " + binary_gap(529));
	console.log("binary_gap(20); expect 1: " + binary_gap(20));
	console.log("binary_gap(15); expect 0: " + binary_gap(15));
	// codility testing:
	/// https://app.codility.com/programmers/lessons/1-iterations/binary_gap/
	/// note: function must be renamed "solution" for testing
	/// performance: not assessed
	/// correctness: 100%
	/// Difficulty: Painless
