from typing import List, Optional


def myPow(x: float, n: int) -> float:
    """
    time complexity: log(n)
    space complexity: log(n)
    """

    def reduce_exp(x, n):
        
        if x == 0:
            return 0
        if n == 0:
            return 1
        
        res = reduce_exp(x, n // 2)
        res = res * res

        return x * res if n % 2 == 1 else res 

    result = reduce_exp(x, abs(n))

    if n < 0:
        return 1/result
    return result



if __name__ == "__main__":

    # test cases
    x = 2
    n = 10

    ret = myPow(x, n)
    print(ret)
