
from bank import bankoper

def test_deposit():
    totalbalance, updatedbalance = bankoper(200000, 30000, 0)

    assert totalbalance == 230000
    assert updatedbalance == 230000


def test_withdraw():
    totalbalance, updatedbalance = bankoper(100000, 40000, 10000)

    assert totalbalance == 140000
    assert updatedbalance == 130000


def test_anyamount():
    totalbalance, updatedbalance = bankoper(15000, 0, 15000)

    assert totalbalance == 15000
    assert updatedbalance == 0
