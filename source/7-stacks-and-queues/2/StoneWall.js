// Cover 'Manhattan skyline' using the minimum number of rectangles. 
function StoneWall(H) {
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
var result = StoneWall(args);
// eslint-disable-next-line no-console
console.log('JavaScript result: ' + result);
// Codility Testing:
/// https://app.codility.com/demo/results/trainingSTMQVS-DX6/
/// Correctness: 100%
/// Performance: 77%
/// Difficulty: Painless
