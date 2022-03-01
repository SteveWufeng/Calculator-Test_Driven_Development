import Calculator

def testAdd():
    #setup
    input = "2 + 5"
    expected = 7

    #invoke
    actual = Calculator.add(input)

    #analyse
    assert (expected == actual)

def testAddBigNumbers():
    #setup
    input = "999 + 999"
    expected = 1998

    #invoke
    actual = Calculator.add(input)

    #analyse
    assert (expected == actual)

def testMinus():
    #setup
    input = "100 - 20"
    expected = 80

    #invoke
    actual = Calculator.minus(input) 

    #analyse
    assert (expected == actual)