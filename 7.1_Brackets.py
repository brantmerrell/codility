# Determine whether a given string of parentheses is properly nested
# Bash Testing:

def Brackets(S):
	# split string into array
	S = list(S)
	# create object to match lefts and rights
	match = {"]":"[","}":"{",")":"("}
	lefts = ["{","[","("]
	# create stack to track bracket matches
	stack = []
	# loop through S
	for i in range(0,len(S)):
		# test for leftness
		if S[i] in lefts:
			# if left, add to stack
			stack.append(S[i])
		# if right, make sure stack already has an element
		elif len(stack)!=0:
			# remove an element from stack
			POP = stack.pop()
			# removed element should equal S[i]
			if match[S[i]]!=POP:
				# if not, return zero
				return(0)
	# if stack.length==0 after loop finishes, the lefts and right 'balance'
	if len(stack)==0:
		return(1)
	# otherwise, they do not
	else:
		return(0)

# Bash Testing:
import getopt, sys, re, datetime
args = list(getopt.getopt(sys.argv,"ho:v"))[1][1]
#args = re.sub("^\[|\]$","",args).split(",")
#args = [int(x) for x in args]
time1 = datetime.datetime.now()
result = Brackets(args)
time2 = datetime.datetime.now()
timeChange = time2-time1
print(["result: "]+[result]+[" ; milliseconds: "]+[timeChange.total_seconds()*1000])
# Codility Testing:
## https://app.codility.com/demo/results/trainingB73C4A-TQM/
## Correctness: 100%
## Performance: 80%
## Difficulty: Painless


