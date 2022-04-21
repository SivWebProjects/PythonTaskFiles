def sum(num1, num2):
    """Returns the sum of two numbers

        Parameters:
            num1 (int): First integer number
            num2 (int): Second integer number
        Returns:
            result (num): An integer
    """
    result = num1 + num2
    return result


def subtraction(num1, num2):
    """Returns the difference of two numbers

        Parameters:
            num1 (int): First integer number
            num2 (int): Second integer number
        Returns:
            result (num): An integer
    """
    result = num1 - num2
    return result


def multiplication(num1, num2):
    """Returns the product of two numbers

        Parameters:
            num1 (int): First integer number
            num2 (int): Second integer number
        Returns:
            result (num): An integer
    """
    result = num1 * num2
    return result


def division(num1, num2):
    """Performs division and returns quotient

        Parameters:
            num1 (int): First integer number
            num2 (int): Second integer number
        Returns:
            result (float): A float rounded by 3 decimals
    """
    result = num1 / num2
    result = round(result, 3)
    return result
