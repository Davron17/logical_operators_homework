def main(n):
    """
    A number consisting of one and zero is given (the number starts at once). 
    If the number of ones is greater than zero, true, otherwise False is returned.
    
    Args:
        n(int): parameter n
    Returns:
        bool: answer
    """

    return n%10==1 and n//10000<=1 and (n-n//10000*10000)//1000<=1 and (n-n//1000*1000)//100<=1 and (n-n//100*100)//10<=1
print(main(11000))
print(main(1101))