import pytest

"""
@pytest.mark.<groupname>
@pytest.mark.<builin> #skip  #xfail

"""
@pytest.mark.skip
def test_first():
    assert 3+2==5
    print("test_first pass")

@pytest.mark.regression
def test_3rd():
    print("test_3rd pass")


@pytest.mark.regression
def test_sencond():
    assert 3+2==5
    print("test_sencond pass")
@pytest.mark.xfail
def test_4th():
    print("test_4th pass")