
# TODO


def test_DAI(DAI, accounts):
    assert DAI.decimals() == 18

    DAI._mint_for_testing(10000000, {'from': accounts[0]})
    assert DAI.balanceOf(accounts[0]) == 10000000

    tx = DAI.transfer(accounts[1], 1000, {'from': accounts[0]})
    assert tx.return_value is True


def test_USDT(USDT, accounts):
    assert USDT.decimals() == 6

    USDT._mint_for_testing(10000000, {'from': accounts[0]})
    assert USDT.balanceOf(accounts[0]) == 10000000

    tx = USDT.transfer(accounts[1], 1000, {'from': accounts[0]})
    assert tx.return_value is None
