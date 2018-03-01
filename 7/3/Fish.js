// N voracious fish are moving along a river. Calculate how many fish are alive.
function Fish(arr_a,arr_b) {
    // begin with a fishCount of array lengths
    var fishCount = arr_a.length;
    // identify lowest index travelling up arrays
    var upMax = 0; // begin at zero
    // increase until arr_b[upMax]==1
    while(arr_b[upMax]!=1 & upMax<arr_b.length){
        upMax+=1;
    }
    // identify highest index travelling down arrays
    var downMax = arr_a.length-1; // begin at last index
    // decrease until arr_b[downmax]==0
    while(arr_b[downMax]!=0 & 0<=downMax){
        downMax-=1;
    }
    // loop through indices of arrays
    for(var ndx_i=0; ndx_i<arr_a.length; ndx_i++){
        // travel up the array to identify when direction 1 eats direction 0
        // only adjust upMax upwards when ndx_i-fish is direction 1 and larger than upMax
        // if upMax is smaller than up-traveling fish ndx_i
        if(arr_b[ndx_i]==1 && arr_a[upMax]<arr_a[ndx_i]){ 
            upMax=ndx_i; // adjust upMax
        }
        // if upMax is smaller than down-traveling fish, adjust upMax to next up-travelling fish
        if(arr_a[upMax] < arr_a[ndx_i] && arr_b[ndx_i]==0){
            while(arr_b[upMax]!=1 & upMax<=arr_b.length){
                upMax+=1;
            }
        }
        // only subtract if upMax is downstream of indexFish
        // only subtract if indexFish travels down
        // only subtract if the indexFish is smaller than upMax  
        if(upMax<ndx_i && arr_b[ndx_i]==0 && arr_a[ndx_i]<arr_a[upMax]){
            fishCount-=1;
        }
        // travel down the array to identify when direction 0 eats direction 1
        // if index direction is 0 and downMax is smaller than index size, 
        if(arr_b[ndx_i]==0 && arr_a[downMax]<arr_a[ndx_i]){
            // set new downMax
            downMax=ndx_i;
        }
        // if downMax is smaller than ndx_i-fish and ndx_i-fish is traveling direction 1, it gets eaten
        // the subtraction is handled in the other direction, but new downMax needs to be defined 
        if(arr_a[downMax] < arr_a[ndx_i] && arr_b[ndx_i]==1){
            while(arr_b[downMax]!=0 && 0<= downMax){
                downMax-=1;
            }
        }
        // if downMax is upStream of indexFish, indexFish travels up, 
        // and index fish is smaller than downMax,
        if(ndx_i<downMax && arr_b[ndx_i]==1 && arr_a[ndx_i]<arr_a[downMax]){
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
/// https://app.codility.com/demo/results/training42TT5X-QKF/; 
/// trainingXFRTM3-GER - continuous while loop issue
/// Correctness: 75% - consistently not subtracting enough
/// Performance: 50%
/// Difficulty: Painless
