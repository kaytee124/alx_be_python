# arithmetic_operations.py

def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform basic arithmetic operations (add, subtract, multiply, divide) 
    based on the input operation string.

    Args:
    num1 (float): The first number.
    num2 (float): The second number.
    operation (str): The arithmetic operation to perform ("add", "subtract", "multiply", "divide").

    Returns:
    float or str: The result of the operation, or an error message if division by zero or invalid operation.
    """
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 != 0:
                return num1 / num2
            else:
                return "Error: Division by zero"
        case _:
            return "Error: Invalid operation"
