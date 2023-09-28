class Variable:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Predicate:
    def __init__(self, name, arity):
        self.name = name
        self.arity = arity

    def __str__(self):
        return self.name

class Atom:
    def __init__(self, predicate, arguments):
        self.predicate = predicate
        self.arguments = arguments

    def __str__(self):
        return f"{self.predicate}({', '.join(map(str, self.arguments))})"

class And:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f"({self.left} ∧ {self.right})"

class Or:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f"({self.left} ∨ {self.right})"

class Implies:
    def __init__(self, antecedent, consequent):
        self.antecedent = antecedent
        self.consequent = consequent

    def __str__(self):
        return f"({self.antecedent} → {self.consequent})"

# Example usage
x = Variable("x")
y = Variable("y")
apple = Predicate("apple", 1)
banana = Predicate("banana", 1)

# Create atomic statements (atoms) using the predicates
atom1 = Atom(apple, [x])
atom2 = Atom(apple, [y])
atom3 = Atom(banana, [x])

expression1 = Implies(And(atom1, atom2), Or(atom1, atom3))

print("Expression 1:", expression1)
