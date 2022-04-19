def finding_palindrome(num):
    """
    Returns given integer is a palindrome or not.

            Parameters:
                    num (int): An integer

            Returns:
                    binary_sum (bool): A Boolean
    """

    # When number < 0, number is not a palindrome.
    # Also, if the last digit of the number is 0, in order to be a palindrome,
    # The first digit of the number also needs to be 0.
    # Only 0 satisfy this property.
    if num < 0 or ((num % 10 == 0) and num != 0):
        return False

    rev_num = 0
    while num > rev_num:
        rem = num % 10
        rev_num = rev_num * 10 + rem
        num //= 10

    # When the length is an odd number, we can get rid of the middle digit by rev_num / 10
    # For example when the input is 12321, at the end of the while loop we get x = 12, rev_num = 123,
    # Since the middle digit doesn't matter in palindrome(it will always equal to itself), we can simply get rid of it.
    return num == rev_num or num == rev_num // 10


num = int(input("Enter an integer number: "))

result = finding_palindrome(num)
print(result)

"""
# Finding given number is a palindrome or not by taking number as a string
num = input("Enter an integer number: ")
reverse_num = num[-1::-1]

if num == reverse_num:
    return True

else:
    return False
"""
