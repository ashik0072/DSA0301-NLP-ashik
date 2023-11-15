import nltk
from nltk import CFG

# Define a context-free grammar for FOPC expressions
fopc_grammar = CFG.fromstring("""
    S -> VARIABLE PREDICATE VARIABLE | QUANTIFIER VARIABLE PREDICATE
    VARIABLE -> 'x' | 'y' | 'z'
    PREDICATE -> 'P' | 'Q' | 'R'
    QUANTIFIER -> 'forall' | 'exists'
""")

# Create an NLTK parser
fopc_parser = nltk.ChartParser(fopc_grammar)


def parse_fopc(expression):
    try:
        tokens = expression.split()
        parses = list(fopc_parser.parse(tokens))
        if parses:
            return parses[0]
        else:
            print("No valid parse for the expression.")
            return None
    except Exception as e:
        print(f"Error parsing expression: {e}")
        return None


if __name__ == "__main__":
    # Example FOPC expressions
    expression1 = "forall x P x"
    expression2 = "exists y Q y"

    # Parse and print the results
    result1 = parse_fopc(expression1)
    result2 = parse_fopc(expression2)

    if result1:
        print("Parsed Expression 1:")
        result1.pretty_print()

    if result2:
        print("Parsed Expression 2:")
        result2.pretty_print()
