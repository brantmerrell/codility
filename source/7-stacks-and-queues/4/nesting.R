# Determine whether a given string of parentheses (single type) is properly nested.
nesting <- function(str_s){
  # set the balance of parentheses at zero
  balance <- 0
  # convert string to vector
  str_s <- strsplit(str_s, "")[[1]]
  # iterate through the vector of parentheses
  for(paren in str_s){
    # if parenthesis is left, add to balance; otherwise, subtract
    ifelse(paren == "(", balance <- balance + 1, balance <- balance - 1)
      # there should never be more right parentheses
    if(balance < 0){
      return(0)
    }
  }
  # a balance of zero indecates balance
  return(ifelse(balance == 0, 1, 0))
}
# Debugging:
# print(nesting("())"))
# print(nesting("(()(())())"))
# Bash Testing:
ARGS_S <- commandArgs()[6]
print(nesting(ARGS_S))