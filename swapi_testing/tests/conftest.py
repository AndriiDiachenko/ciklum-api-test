import pytest
from time import time

@pytest.fixture(scope='function', autouse=True)
def timer(request):
        def timer_wraper():
            print(' Time spend:  %s' % str(request.node.rep_call.duration)[0:7])

        request.addfinalizer(timer_wraper)

@pytest.mark.tryfirst
def pytest_runtest_makereport(item, call, __multicall__):
    rep = __multicall__.execute()
    setattr(item, "rep_" + rep.when, rep)
    return rep

