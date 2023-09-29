def main(a):
    """
    Given a five-digit integer a,  check the following statement "All digits of the number are in ascending order".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return a//10000>(a-a//10000*10000)//1000>(a-a//1000*1000)//100>(a-a//100*100)//10>(a-a//100*100)%10
print(main(54321))
print(main(11234))