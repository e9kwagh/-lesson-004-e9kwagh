def is_palindrome(n):
    return str(n) == str(n)[::-1]

def answer():
    """ Find the largest palindrome made from the product
      of two 3-digit numbers."""
    start = 101
    end = 999
    greater = 0
    for i in reversed(range(start, end)):
        for num in reversed(range(start, i + 1)):  # Include i in the range
            product = i * num
            if product <= greater:
                # Break the inner loop if the product is less than or equal to the current maximum palindrome.
                break
            if is_palindrome(product):
                greater = product

    return greater

if __name__ == "__main__":
    print(answer())
