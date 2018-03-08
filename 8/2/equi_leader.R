# count the number of equi-leaders
equi_leader <- function(vec_a){
    # start equi_count at zero
    equi_count <- 0
    # create table of value counts
    tab_r <- table(vec_a)
    # create table of zero counts, names equal to tab_r
    tab_l <- rep(0,length(tab_r))
    names(tab_l) <- names(tab_r)
    # iterate through elements of vec_a
    for(elem in vec_a){
        # convert class of element to character
        elem <- as.character(elem)
        # subtract element from righthand counts
        tab_r[elem] <- tab_r[elem] - 1
        # add element to lefthand counts
        tab_l[elem] <- tab_l[elem] + 1
        # define lead for righthand split
        lead_a <- names(tab_r[sum(tab_r) / 2 < tab_r])
        # define lead for lefthand split
        lead_b <- names(tab_l[sum(tab_l) / 2 < tab_l])
        # if both leads exist, 
        if(length(lead_a) == 1 & length(lead_b) == 1){
          # and are equivalent
          if(lead_a == lead_b){
            # add to equi_count
            equi_count <- equi_count + 1
          }
        }
    }
    return(equi_count)
}
# debugging
# VEC_A <- c(4, 3, 4, 4, 4, 2)
# equi_leader(VEC_A)
# Bash Testing:
VEC_A <- commandArgs()[6] # store arguments passed from command line
VEC_A <- gsub("\\]|\\[", "", VEC_A) # remove brackets
VEC_A <- unlist(strsplit(VEC_A, ", *")) # convert to vector
print(equi_leader(VEC_A))

