class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else ('EOF', None)

    def eat(self, expected_type):
        token = self.peek()
        if token[0] == expected_type:
            self.pos += 1
            return token
        raise RuntimeError(f'Expected {expected_type} but got {token[0]}')

    def parse(self):
        return self.expr()

    def expr(self):  # expr -> term ((PLUS|MINUS) term)*
        result = self.term()
        while self.peek()[0] in ('PLUS', 'MINUS'):
            op = self.eat(self.peek()[0])[0]
            rhs = self.term()
            result = result + rhs if op == 'PLUS' else result - rhs
        return result

    def term(self):  # term -> factor ((TIMES|DIVIDE) factor)*
        result = self.factor()
        while self.peek()[0] in ('TIMES', 'DIVIDE'):
            op = self.eat(self.peek()[0])[0]
            rhs = self.factor()
            result = result * rhs if op == 'TIMES' else result / rhs
        return result

    def factor(self):  # factor -> NUMBER | (expr)
        token = self.peek()
        if token[0] == 'NUMBER':
            return self.eat('NUMBER')[1]
        elif token[0] == 'LPAREN':
            self.eat('LPAREN')
            result = self.expr()
            self.eat('RPAREN')
            return result
        raise RuntimeError('Expected NUMBER or LPAREN')
