// N voracious fish are moving along a river. Calculate how many fish are alive.
function Fish(H) {
    // start block count at 1
    var blocks = H.length;
    // iterate through H to compare blocks
    for (var n = 0; n < H.length; n++) {
        // create a lookback variable to crawl backwards from current loop location
        var lookback = n;
        // only crawl backwards while height is high enough to share stones
        while ((H[n] <= H[lookback]) && (0 < lookback)) {
            lookback -= 1;
            // if a shared height is reached, 
            if (H[lookback] == H[n]) {
                // subtract from block count
                blocks -= 1;
                // and stop while loop
                lookback = 0;
            }
        }
    }
    // return the block count
    return (blocks);
}
// Bash Testing:
// import { } from 'node';
var args = process.argv[2].replace(/^\[|\]$/g, '').split(',').map(function (item) { return (parseInt(item)); });
// var time1 = Date.now();
var result = Fish(args);
// var time2 = Date.now();
// eslint-disable-next-line no-console
console.log('result: ' + result); //+ ' ; milliseconds: ' + (time2 - time1));
// Codility Testing:
/// https://app.codility.com/demo/results/trainingSTMQVS-DX6/
/// Correctness:
/// Performance:
/// Difficulty: Painless
