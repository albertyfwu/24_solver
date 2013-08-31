ops = '+-*/'
associative_ops = '+*'

class Expr:
	def __init__(self):
		pass

class Binary(Expr):
	def __init__(self, left, op, right):
		self.left = left
		self.op = op
		self.right = right

	def eval(self):
		return eval(str(self.left.eval()) + self.op + str(self.right.eval()))

	def __str__(self):
		return '(%s %s %s)' % (self.left.__str__(), self.op, self.right.__str__())

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other):
		if type(self) != type(other):
			return False

		if self.op != other.op:
			return False

		if self.left == other.left and self.right == other.right:
			return True

		return False

	def __hash__(self):
		return hash((self.left, self.op, self.right))

class Constant(Expr):
	def __init__(self, x):
		self.x = x

	def eval(self):
		return self.x

	def __str__(self):
		return str(self.x)

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other):
		if type(self) != type(other):
			return False

		return self.x == other.x

	def __hash__(self):
		return hash((self.x))


if __name__ == '__main__':
	expr = Binary(Binary(Constant(5), '-', Binary(Constant(1), '/', Constant(5.0))), '*', Constant(5))
	print expr.eval()
	print expr