// FrogJmp: count minimal number of jumps from X to Y
// Assumptions:
/// Y <= X
/// 1 <= X, Y, & D <= 1,000,000,000
/// X, Y, & D are integers
function FrogJmp(X, Y, D){
	// define distance as Y - X
	var dist_ = Y - X 
	// define jump as (Y-X)/Distance
	var jump_ = dist_ / D 
	// round upwards:
	return(Math.ceil(jump_))
}
// console testing:
// expect answer (85-10)/30 rounded up to 3 jumps
console.log("practice example: X=10, Y=85, D=30. Expect 3:"+FrogJmp(10,85,30)) 
console.log("large text: X = 10000, Y=85000, D=30000. Expect 3:"+FrogJmp(10000,85000,30000))
console.log("suppose Y=X? X=85, Y=85, D=30. Expect 0:"+FrogJmp(85,85,30)) 
console.log("suppose (Y-X)<D? X=6, Y=8, D=3. Expect 1:"+FrogJmp(6,8,3))
// Codility testing: 
/// https://app.codility.com/programmers/lessons/3-time-complexity/frog_jmp/
/// performance: 100% 
/// correctness: 100%
/// Difficulty: Painless
