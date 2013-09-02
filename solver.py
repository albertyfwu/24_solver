from expression import *
from itertools import permutations

game_goal = 24
ops = '+-*/'

def init(nums):
  """Initialize a list of Constant instances given a list of numbers."""
  result = []
  for num in nums:
    result.append(Constant(num))
  return result

def gen(exprs):
  """Given a list of expressions, generates a list of all possible expressions
  using all of the given expressions."""
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
  """Given a list of numbers and a goal number, solves for ways to apply
  addition, subtraction, multiplication, division to the list of numbers
  to obtain the goal number."""
  result = set()
  inits = init(nums)
  inits_list = permutations(inits)

  for inits in inits_list:
    for expr in gen(inits):
      if abs(expr.eval() - goal) < 0.001:
        result.add(expr)
  return result

def disp(exprs):
  """Print the list of expressions line by line."""
  for expr in exprs:
    print expr

if __name__ == '__main__':
  while True:
    raw = raw_input("Enter a list of numbers: ")

    # process
    raw_list = [int(elem) for elem in raw.strip(',').replace(' ', '').split(',')]

    print 'Solutions:'
    disp(solve(raw_list, game_goal))
    print 'End of Solutions\n'
