def main(a):
    """
    Given a three-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return (a//100+(a-a//100*100)//10+(a-a//100*100)%10)%2==1.0
print(main(152))
print(main(335))