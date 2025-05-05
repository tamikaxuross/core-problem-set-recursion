# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    return n * factorial(n - 1)


# reverse
def reverse(text):
    if len(text) <= 1:
        return text
    return text[-1] + reverse(text[:-1])


# bunny
def bunny(count):
    if count == 0:
        return 0
    return 2 + bunny(count - 1)


# is_nested_parens
def is_nested_parens(parens):
    def helper(start, end):
        if start > end:
            return True
        if parens[start] != '(' or parens[end] != ')':
            return False
        return helper(start + 1, end - 1)

    return helper(0, len(parens) - 1)

