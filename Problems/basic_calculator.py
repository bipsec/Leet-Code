class BasicCalculator:
    def __init__(self):
        pass
        # print("Basic Calculator Initialized. Enter 'exit' to quit.")

    def evaluate(self, expression):
        try:
            # Tokenize the expression and compute the result
            tokens = self.tokenize(expression)
            postfix = self.infix_to_postfix(tokens)
            result = self.evaluate_postfix(postfix)
            return result
        except Exception as e:
            return f"Error: {e}"

    def tokenize(self, expression):
        # Tokenize the input string into numbers and operators
        tokens = []
        number = ""
        for char in expression:
            if char.isdigit() or char == '.':  # Handle numbers
                number += char
            elif char in "+-*/()":  # Handle operators and parentheses
                if number:
                    tokens.append(float(number))  # Append number if it exists
                    number = ""
                tokens.append(char)
            elif char.isspace():  # Skip whitespace
                continue
            else:
                raise ValueError(f"Invalid character: {char}")
        if number:  # Add any remaining number
            tokens.append(float(number))
        return tokens

    def infix_to_postfix(self, tokens):
        # Convert infix expression to postfix using the Shunting Yard algorithm
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        output = []
        operators = []

        for token in tokens:
            if isinstance(token, float):  # If it's a number
                output.append(token)
            elif token in "+-*/":  # If it's an operator
                while (operators and operators[-1] != '(' and
                       precedence[operators[-1]] >= precedence[token]):
                    output.append(operators.pop())
                operators.append(token)
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    output.append(operators.pop())
                if not operators:
                    raise ValueError("Mismatched parentheses")
                operators.pop()  # Remove the '('

        while operators:  # Append remaining operators
            if operators[-1] == '(':
                raise ValueError("Mismatched parentheses")
            output.append(operators.pop())

        return output

    def evaluate_postfix(self, postfix):
        # Evaluate a postfix expression
        stack = []
        for token in postfix:
            if isinstance(token, float):  # Push numbers to the stack
                stack.append(token)
            elif token in "+-*/":
                if len(stack) < 2:
                    raise ValueError("Invalid expression")
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    if b == 0:
                        raise ZeroDivisionError("Division by zero")
                    stack.append(a // b)
        if len(stack) != 1:
            raise ValueError("Invalid expression")
        return stack[0]


class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")

        # chatgpt code
        calculator = BasicCalculator()

        result = calculator.evaluate(s)
        # print("Result:", int(result))
        return int(result)


s = Solution()
print(s.calculate(s="3+2*2"))
print(s.calculate(s=" 3/2 "))
print(s.calculate(s=" 3+5 / 2 "))
print(s.calculate(s=" 4 * 3 + 2 / 2 + 13 -7 + 26"))
