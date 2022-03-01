"""
Test driven development
Author: Steve Wufeng
"""

def add (val1, val2) -> int:
    """
    function that does addition operation
    @param val1: String
    @param val2: String
    @return int
    """
    # TODO: add values and return result
    return 

def minus (val1, val2) -> int:
    """
    function that does subtraction operation
    @param val1: String
    @param val2: String
    @return int
    """
    # TODO: subtract values and return result
    return

def main ():
    user_input = input(">>Enter your operation: ")
    user_input = user_input.split(" ")
    print("your result is: " + add(user_input[0], user_input[2]) + "!")
    