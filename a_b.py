# Function to evaluate the expression
def evaluate_expression(expression):
    # Split the expression into two integers
    a, b = map(int, expression.split('+'))
    # Calculate the sum
    result = a + b
    return result

# Number of test cases
t = int(input( ))

# Iterate through each test case
for _ in range(t):
    # Read the expression
    expression = input()
    # Evaluate the expression and print the result
    print(evaluate_expression(expression))
