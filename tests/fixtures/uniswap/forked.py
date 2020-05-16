import pytest


@pytest.fixture(scope="module")
def uniswap_factory(Contract):
    yield Contract("0xc0a47dFe034B400B47bDaD5FecDa2621de6c4d95")


@pytest.fixture(scope="module")
def uniswap_dai(Contract):
    yield Contract("0x2a1530C4C41db0B0b2bB646CB5Eb1A67b7158667")


@pytest.fixture(scope="module")
def uniswap_usdt(Contract):
    yield Contract("0xc8313c965C47D1E0B5cDCD757B210356AD0e400C")


@pytest.fixture(scope="module")
def uniswap_usdc(Contract):
    yield Contract("0x97deC872013f6B5fB443861090ad931542878126")


@pytest.fixture(scope="module")
def uniswap_susd(Contract):
    yield Contract("0xB944d13b2f4047fc7bd3F7013bcf01b115fb260d")


@pytest.fixture(scope="module")
def uniswap_tusd(Contract):
    yield Contract("0x5048b9d01097498Fd72F3F14bC9Bc74A5aAc8fA7")


@pytest.fixture(scope="module")
def uniswap_busd(Contract):
    yield Contract("0x25C610eeE8f59768c26567c388986Aab3467a3E3")
