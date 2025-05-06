# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if not array:
        return False
    if array[0] == query:
        return True
    return search(array[1:], query)


# is_palindrome
def is_palindrome(text):
    def helper(left, right):
        if left >= right:
            return True
        if text[left] != text[right]:
            return False
        return helper(left + 1, right - 1)

    return helper(0, len(text) - 1)


# digit_match
def digit_match(apples, oranges):
    if apples == 0 or oranges == 0:
        return 1 if apples == 0 and oranges == 0 else 0

    match = 0
    if apples % 10 == oranges % 10:
        match = 1

    remaining_apples = apples // 10
    remaining_oranges = oranges // 10

    if remaining_apples == 0 and remaining_oranges == 0:
        return match

    return match + digit_match(remaining_apples, remaining_oranges)

