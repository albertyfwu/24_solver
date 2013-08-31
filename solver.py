from expression import *
from itertools import permutations

def init(nums):
	result = []
	for num in nums:
		result.append(Constant(float(num)))
	return result

def gen(exprs):
	# given a list of expressions, generates a list of all possible expressions
	if len(exprs) == 1:
		return exprs
	else:
		result = []
		# for all possible dividers
		for i in xrange(1, len(exprs)):
			left, right = exprs[:i], exprs[i:]
			gen_lefts = gen(left)
			gen_rights = gen(right)

			for gen_left in gen_lefts:
				for gen_right in gen_rights:
					for op in ops:
						if not (op == '/' and gen_right.eval() == 0):
							# avoid division by zero
							result.append(Binary(gen_left, op, gen_right)) 
		return result

def solve(nums, goal):
	result = set()
	inits = init(nums)
	inits_list = permutations(inits)

	for inits in inits_list:
		for expr in gen(inits):
			if abs(expr.eval() - goal) < 0.001:
				result.add(expr)
	return result

def disp(exprs):
	for expr in exprs:
		print expr

if __name__ == '__main__':
	while True:
		raw = raw_input("Enter a list of numbers: ")

		# process
		raw = raw.replace(' ', '')
		raw = raw.strip(',')
		raw_list = raw.split(',')
		raw_list = [int(elem) for elem in raw_list]

		print 'Solutions:'
		disp(solve(raw_list, 24))
		print 'End of Solutions\n'