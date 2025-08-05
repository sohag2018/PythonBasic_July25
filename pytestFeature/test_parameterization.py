
import pytest
#approach-1
@pytest.mark.parametrize("num1,num2,sum",[(2,3,5),(5,3,5)])
def test_add(num1, num2,sum):
    assert num1 + num2 == sum

#approach-2--didnt work
# #@pytest.fixture(params=["mizi", "sohag"])
# @pytest.fixture(params=[2,3,5])
# def test_login(request):
#     print(request.param)