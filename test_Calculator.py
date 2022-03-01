import Calculator

def testAdd1():
    #setup
    val1 = "2"
    val2 = "5"
    expected = 7

    #invoke
    actual = Calculator.add(val1, val2)

    #analyse
    assert (expected == actual)

def testAdd2():
    #setup
    val1 = "999"
    val2 = "999"
    expected = 1998

    #invoke
    actual = Calculator.add(val1, val2)

    #analyse
    assert (expected == actual)

def testMinus1():
    #setup
    val1 = "12"
    val2 = "6"
    expected = 6

    #invoke
    actual = Calculator.add(val1, val2)

    #analyse
    assert (expected == actual)

def testMinus2():
    #setup
    val1 = "555"
    val2 = "55"
    expected = 500

    #invoke
    actual = Calculator.add(val1, val2)

    #analyse
    assert (expected == actual)