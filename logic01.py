def main(a,b,c):
    """
    Given three integers a, b, c,  check the following statement "The number b is between a and c".
    Args:
        a(int): parameter a
        b(int): parameter b
        c(int): parameter c
    Returns:
        bool: answer
    """
    return (a+c)/2==b
print(main(3,4,5))
print(main(6,4,5))
print(main(6,4,1))