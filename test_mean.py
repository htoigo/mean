from mean import mean, std
from numpy.testing import assert_allclose

# mean() tests

def test_ints():
    num_list = [1, 2, 3, 4, 5]
    obs = mean(num_list)
    exp = 3
    assert obs == exp

def test_zero():
    num_list = [0, 2, 4, 6]
    obs = mean(num_list)
    exp = 3
    assert obs == exp

def test_double():
    num_list = [1, 2, 3, 4]
    obs = mean(num_list)
    exp = 2.5
    assert obs == exp

def test_long():
    bignum = 100000000
    obs = mean(range(1, bignum))
    exp = bignum / 2.0
    assert obs == exp

def test_complex():
    # Given that complex numbers are an unordered field,
    # the arithmetic mean of complex numbers is meaningless.
    num_list = [2 + 3j, 3 + 4j, -32 - 2j]
    obs = mean(num_list)
    exp = NotImplemented
    assert obs == exp


# std() tests

def test_std1():
    obs = std([0.0, 2.0])
    exp = 1.0
    assert obs == exp

def test_std2():
    obs = std([])
    exp = 0.0
    assert obs == exp

def test_std3():
    obs = std([5.0])
    exp = 0.0
    assert obs == exp

def test_std4():
    obs = std([1.0, 2.0, 3.0, 4.0, 5.0])
    exp = 1.41421
    assert_allclose(obs, exp, atol=0.00001, rtol=0)

def test_std5():
    obs = std([11.0, 11.0, 11.0, 11.0, 11.0, 11.0])
    exp = 0.0
    assert obs == exp
