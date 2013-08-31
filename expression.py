ops = '+-*/'

class Expr:
  def __init__(self):
    pass

class Binary(Expr):
  def __init__(self, left, op, right):
    self.left = left
    self.op = op
    self.right = right

  def eval(self):
    return eval(str(float(self.left.eval())) + self.op + str(float(self.right.eval())))

  def __str__(self):
    return '(%s %s %s)' % (self.left.__str__(), self.op, self.right.__str__())

  def __repr__(self):
    return self.__str__()

  def __eq__(self, other):
    if isinstance(other, Binary):
      return (self.left, self.op, self.right) == (other.left, other.op, other.right)
    return NotImplemented

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
    if isinstance(other, Constant):
      return self.x == other.x
    return NotImplemented

  def __hash__(self):
    return hash((self.x))
