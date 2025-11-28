import pytest


@pytest.fixture(params = ["Chrome", "Firefox", "Opera", ])
def browser(request):
     return request.param

def test_browser_launch(browser):
    print(f" running test on : {browser}")
    assert browser in ["Chrome", "Firefox", "Opera"]