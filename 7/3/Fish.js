// N voracious fish are moving along a river. Calculate how many fish are alive.
function Fish(A,B) {
    // begin with a fishCount of arrays.length
    var fishCount = A.length;
    // identify lowest index travelling up arrays
    var upMax = 0; // begin at zero
    // increase until B[upMax]==1
    while(B[upMax]!=1){
        upMax+=1;
    }
    // identify highest index travelling down arrays
    var downMax = A.length-1; // begin at last index
    // decrease until B[downmax]==0
    while(B[downMax]!=0){
        downMax-=1;
    }
    // loop through indices of arrays
    for(var i=0; i<A.length; i++){
        // travel up the array to identify when direction 1 eats direction 0
        // only adjust upMax upwards when i-fish is direction 1 and larger than upMax
        if(B[i]==1 && A[upMax]<A[i]){ // if upMax is smaller than up-traveling fish i,
            upMax=i; // adjust upMax
        }
        // if upMax is smaller than down-traveling fish, adjust upMax to next up-travelling fish
        if(A[upMax] < A[i] && B[i]==0){
            while(B[upMax]!=1 & upMax<=B.length){
                upMax+=1;
            }
        }
        // only subtract if upMax is downstream of indexFish
        // only subtract if indexFish travels down
        // only subtract if the indexFish is smaller than upMax  
        if(upMax<i && B[i]==0 && A[i]<A[upMax]){
            fishCount-=1;
        }
        // travel down the array to identify when direction 0 eats direction 1
        // if index direction is 0 and downMax is smaller than index size, 
        if(B[i]==0 && A[downMax]<A[i]){
            // set new downMax
            downMax=i;
        }
        // if downMax is smaller than i-fish and i-fish is traveling direction 1, it gets eaten
        // the subtraction is handled in the other direction, but new downMax needs to be defined 
        if(A[downMax] < A[i] && B[i]==1){
            while(B[downMax]!=0 && 0<= downMax){
                downMax-=1;
            }
        }
        // if downMax is upStream of indexFish, indexFish travels up, 
        // and index fish is smaller than downMax,
        if(i<downMax && B[i]==1 && A[i]<A[downMax]){
            // indexFish gets eaten
            fishCount-=1;
        }
    }
    return(fishCount);
}
// Bash Testing:
// import { } from 'node';
// var myPattern = new RegExp('\\],*\\[');
var ARGS_A = process.argv[2].replace(/^\[|\]$/g, '').split(RegExp('\\],*\\['));
var ARGS_B = ARGS_A[1].split(',').map(function (item) { return (parseInt(item)); });
ARGS_A = ARGS_A[0].split(',').map(function (item) { return (parseInt(item)); });
// var time1 = Date.now();
var result = Fish(ARGS_A,ARGS_B);
// var time2 = Date.now();
// eslint-disable-next-line no-console
console.log('result: ' + result); //+ ' ; milliseconds: ' + (time2 - time1));
// Codility Testing:
/// https://app.codility.com/demo/results/trainingXFRTM3-GER/
/// Correctness: 50% - consistently not subtracting enough
/// Performance: 25%
/// Difficulty: Painless
