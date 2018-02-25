// compute the number of disk intersections in a sequence of disks
// Assumptions:
/// 0 <= N <= 100,000
/// 0 <= A[i] <= 2,147,483,647
function NumberOfDiscIntersections(A) {
	// begin with zero intersections
	var intersections = 0;
	// crawl along array A
	for(var i=0; i<A.length; i++){
		console.log("i: "+i+", A[i]: "+A[i])
		// crawl distance "counter" from index, where counter = A[i]
		var counter = 0
		while(counter < A[i]){
			counter = counter + 1
			console.log("    counter: "+counter+
				", A[i+counter]: "+A[i+counter]+
				", A[i-counter]: "+A[i-counter])
			// look ahead of index by distance counter (but not farther than length of A)
			// to avoid double-counting intersections, only count those < A[i]
			if(A[i+counter]<A[i] && (i+counter<A.length)){
				// add to intersections count
				intersections = intersections+1
				console.log("        intersections: ",intersections)
			}
			// look behind index by distance counter (but not lower than zero)
			// to avoid double-counting intersections, only count those <= A[i]
			if(A[i-counter]<=A[i] && (0<=i-counter)){
				// add to intersections count
				intersections = intersections+1
				console.log("        intersections: ",intersections)
			}
		}
	}
	return(intersections)
}
/// Console Testing
//console.log("NumberOfDiscIntersections([1,5,2,1,4,0]); expect 11: " + NumberOfDiscIntersections([1,5,2,1,4,0]));
console.log("NumberOfDiscIntersections([1,1,1]); expect 3: " + NumberOfDiscIntersections([1,1,1]));
// Codility Testing
/// https://app.codility.com/programmers/lessons/6-sorting/number_of_disc_intersections/
/// performance: 12%
/// correctness: 0%
/// Difficulty: Respectable
