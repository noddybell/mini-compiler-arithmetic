from lexer import tokenize
from parser import Parser

def main():
    print("Mini Compiler for Arithmetic Expressions")
    while True:
        try:
            expr = input("\nEnter expression (or type 'exit'): ")
            if expr.lower() == 'exit':
                break
            tokens = tokenize(expr)
            parser = Parser(tokens)
            result = parser.parse()
            print("Result:", result)
        except Exception as e:
            print("Error:", e)

if __name__ == '__main__':
    main()
