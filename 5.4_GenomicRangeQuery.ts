// count the number of passing cars on the road 

// Assumptions:
/// 1 <= N <= 100,000
/// 1 <= M <= 50,000
/// 0 <= P <= N-1
/// 0 <= Q <= N-1
/// Pk <= Qk, where 0 <= k < M
/// string S consists only of uppercase letters A, C, G, T

function GenomicRangeQuery(S,P,Q){
	
	// split S string into vector of characters
	S=S.split("")
	// convert A, C, G, T to 1, 2, 3, 4 respectively
	for(var n=0; n<S.length; n++){
		if(S[n]=="A") S[n]=1
		if(S[n]=="C") S[n]=2
		if(S[n]=="G") S[n]=3
		if(S[n]=="T") S[n]=4
	}
	// create empty result vector
	var res = []
	// build result vector 
	for(var k=0; k<P.length; k++){
		// minimum of range along S from P to Q
		res.push(Math.min.apply(Math,S.slice(P[k],Q[k]+1)))
	}
	return((res))
}

// console testing:
console.log("GenomicRangeQuery('CAGCCTA',2,5,0,4,5,6); expect 2,4,1: "+
	GenomicRangeQuery('CAGCCTA',[2,5,0],[4,5,6]))

// Codility testing:
/// https://app.codility.com/programmers/lessons/5-prefix_sums/genomic_range_query/
/// Performance:
/// Correctness:

/// Difficulty: Respectable
