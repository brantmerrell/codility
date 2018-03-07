# Find an index of an array such that its value occurs at more than half of indices in the array.
dominator <- function(vec_a){
  if(length(vec_a)==0){
    return(-1)
  }
  # use the table function to count the occurrences of each element
  occur <- table(vec_a)
  # use the max function to obtain the value that occurres the most
  value <- as.numeric(names(occur[occur==max(occur)]))
  # list all the indices that correspond to value
  indices <- which(vec_a == value)
  # if length of indices is less than half of length of vec_a, return -1
  if(length(indices) * 2 <= length(vec_a)){
    return(-1)
  }
  # return any of the indices (adjusted to zero-index results)
  return(sample(indices, 1) - 1)
}
# debugging
# VEC_A <- c(3, 4, 3, 2, 3, -1, 3, 3)
# print(dominator(VEC_A) %in% c(0, 2, 4, 6, 7))
# expect degit that corresponds as zero-index to value 3
# Bash Testing:
VEC_A <- commandArgs()[6] # store arguments passed from command line
VEC_A <- gsub("\\]|\\[", "", VEC_A) # remove brackets
VEC_A <- unlist(strsplit(VEC_A, ", *")) # conver to vector
print(dominator(VEC_A))
