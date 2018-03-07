# N voracious fish are moving along a river. Calculate how many fish are alive.
Fish <- function(arr_a, arr_b){
    # begin with a fish_count of zero
    fish_count <- 0
    # keep track of fish traveling downstream
    fish_down <- c()
    # loop through indices of arrays
    for(ndx_i in seq(length(arr_a))) {
        # test whether fish is traveling downstream
        if (arr_b[ndx_i] == 1) {
            # if so, append to fish_down
            fish_down <- c(fish_down,arr_a[ndx_i])
        }
        else {
            # test whether there are any fish it will meet
            while (length(fish_down) != 0) {
                # if so, test whether it will eat the nearest downstream fish
                if (fish_down[length(fish_down)] < arr_a[ndx_i]) {
                    # if so, remove downstream fish from downstream list
                    fish_down <- fish_down[-length(fish_down)]
                    # if the downstream fish will eat the index fish,
                }
                else {
                    break
                }
            }
            # if it meets none or eats all, add it to fish count:
            if (length(fish_down) == 0) {
                # add index fish to survival count
                fish_count <- fish_count + 1
            }
        }
    }
    # downstream fish who remained in the fish_down array have not been 'popped', so add to fish_count
    fish_count <- fish_count + length(fish_down)
    return (fish_count)
}
# Bash Testing:
# ARGS_A <- commandArgs()[6]
# ARGS_A <- gsub("^\\[|\\]$","",ARGS_A)
# ARGS_B <- strsplit(ARGS_A,"\\],? *\\[")[[1]][2]
# ARGS_A <- strsplit(ARGS_A,"\\],? *\\[")[[1]][1]
# ARGS_B <- as.numeric(unlist(strsplit(ARGS_B,", ?")))
# ARGS_A <- as.numeric(unlist(strsplit(ARGS_A,", ?")))
ARGS_A <- c(7947, 21515, 15142, 25406, 4233, 14639, 21604, 4975, 23853, 26088)
ARGS_B <- c(1, 1, 0, 0, 1, 1, 0, 1, 1, 0)
print(paste("result:", Fish(ARGS_A, ARGS_B)))
# Codility Testing:
## Difficulty: Painless
